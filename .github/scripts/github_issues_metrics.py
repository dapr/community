#
# Copyright 2022 The Dapr Authors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# This script collects different metrics out of our activities on GitHub.

import os

from datetime import datetime, timedelta

import humanize
import json
import requests

from dapr.clients import DaprClient
from github import Github

ONE_DAY = timedelta(days=1)
FIVE_DAYS = timedelta(days=5)

githubToken = os.getenv("GITHUB_TOKEN")

my_repos=[
    'dapr',
    'components-contrib']

expected_triage_labels=[
    ('P0', 'P1', 'P2', 'P3'),
    ('pinned', 'triaged/resolved')
]

now=datetime.now().utcnow()

def is_triaged(label_events):
    for expected_label_set in expected_triage_labels:
        # At least one of the labels per set should be present.
        if True not in [l.lower() in label_events for l in expected_label_set]:
            return False
    return True


def get_triaged_time(label_events):
    if not is_triaged(label_events):
        return now
    timestamps = []
    for expected_label_set in expected_triage_labels:
        for label in expected_label_set:
            if label in label_events:
                timestamps = timestamps + [label_events[label]]
    if len(timestamps) == 0:
        return now
    return max(timestamps)

def calculate_e2e_tests_success_rate():
    runsCount = 0
    successRunsCount = 0

    headers = { 
        "Accept" : "application/vnd.github.v3.star+json" , 
        "Authorization" : "token {}".format(githubToken)
    }
    # Query last n runs
    url = 'https://api.github.com/repos/dapr/dapr/actions/workflows/4432/runs?branch=master&event=schedule&status=completed&per_page=100'
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print('Error, status HTTP %d' % (r.status_code))
        return {}

    response = r.json()
    for run in response["workflow_runs"]:
        runsCount += 1
        if run["conclusion"] == 'success':
            successRunsCount += 1

    if runsCount == 0:
        return {}

    return {
        "e2e_test_runs_count" : runsCount,
        "e2e_test_success_runs_count": successRunsCount,
        "e2e_test_success_ratio" : (successRunsCount * 1.0) / runsCount
    }


# using an access token
g = Github(githubToken)

issues_since=datetime.now()-timedelta(days=30)

total_count = 0
triaged_count = 0
triaged_under_5_days_count = 0
expected_total_time_to_triage = timedelta()
total_time_to_triage = timedelta()
triaged_bugs = []
not_triaged_bugs = []

for repo in my_repos:
    # discover milestone project
    issues = [i for i in g.get_repo('dapr/' + repo).get_issues(labels=['kind/bug'], since=issues_since) if i.created_at >= issues_since]
    total_count += len(issues)

    for issue in issues:
        events = sorted(issue.get_events(), key=lambda e:str(e.created_at))
        # Dictionary of the latest time 
        first_label_events = dict()
        for event in events:
            if event.event == 'labeled':
                canonical_label = event.label.name.lower()
                if canonical_label not in first_label_events:
                    first_label_events[canonical_label] = event.created_at
        triaged_time = get_triaged_time(first_label_events)
        time_to_triage = triaged_time - issue.created_at
        expected_total_time_to_triage += time_to_triage
        age_str = humanize.naturaldelta(now - issue.created_at)
        bug = {
                'url': issue.html_url,
                'age': age_str,
        }
        if is_triaged(first_label_events):
            bugs = triaged_bugs
            total_time_to_triage += time_to_triage
            triaged_count += 1
            if time_to_triage.total_seconds() <= FIVE_DAYS.total_seconds():
                triaged_under_5_days_count += 1
            time_to_triage_str = humanize.naturaldelta(time_to_triage)
            bug['time_to_triage'] = time_to_triage_str
            print('Issue %s created %s ago and triaged in %s' % (issue.html_url, age_str, time_to_triage_str))
        else:
            bugs = not_triaged_bugs
            print('Issue %s created %s ago but still not triaged, assuming %s to triage' % (
                issue.html_url, age_str, humanize.naturaldelta(time_to_triage)))
        bugs.append(bug)

average_days_to_triage = (total_time_to_triage / triaged_count).total_seconds() / ONE_DAY.total_seconds()
expected_average_days_to_triage = (expected_total_time_to_triage / total_count).total_seconds() / ONE_DAY.total_seconds()
triaged_under_5_days_ratio = triaged_under_5_days_count / total_count

e2e_tests_metrics = calculate_e2e_tests_success_rate()

output = json.dumps(
    indent=2,
    obj=
    {
        'utc_date': now.strftime('%Y-%m-%d'),
        'utc_timestamp': now.isoformat(),
        'repos': my_repos,
        'triaged_bugs': triaged_bugs,
        'not_triaged_bugs': not_triaged_bugs,
        'metrics': {
            'last_30days_total_bugs': total_count,
            'last_30days_total_bugs_triaged': triaged_count,
            'last_30days_total_bugs_triaged_within_5_days': triaged_under_5_days_count,
            'last_30days_percentage_bugs_triaged_within_5_days': triaged_under_5_days_ratio * 100.0,
            'last_30days_average_days_to_triage': average_days_to_triage,
            'last_30days_expected_average_days_to_triage': expected_average_days_to_triage, 
            'latest_runs_e2e_test_count': e2e_tests_metrics['e2e_test_runs_count'],
            'latest_runs_e2e_test_success_count': e2e_tests_metrics['e2e_test_success_runs_count'],
            'latest_runs_e2e_test_success_ratio': e2e_tests_metrics['e2e_test_success_ratio'],
            'latest_runs_e2e_test_success_percentage': e2e_tests_metrics['e2e_test_success_ratio'] * 100.0,
        }
    })

print("%d issues, %lf %% triaged, %.2lf days on average, %lf %% triaged under 5 days" % (total_count,
      (triaged_count * 100.0) / total_count, expected_average_days_to_triage, triaged_under_5_days_ratio * 100.0))

print(output)
with DaprClient() as d:
    d.wait(60)
    filename ='github_issues_metrics.json'
    resp = d.invoke_binding(
        binding_name='dapr-github-metrics-binding',
        operation='create',
        data=output,
        binding_metadata={
            'blobName': filename,
            'fileName': filename,
        })
    print(resp.json())
