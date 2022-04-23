#
# Copyright 2021 The Dapr Authors
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

from dapr.clients import DaprClient
from github import Github

ONE_DAY = timedelta(days=1)

githubToken = os.getenv("GITHUB_TOKEN")

my_repos=[
    'dapr',
    'components-contrib']

expected_triage_labels=[
    ('P0', 'P1', 'P2', 'P3'),
    ('size/xs', 'size/s', 'size/m', 'size/l', 'size/xl'),
    ('pinned', 'triaged/resolved')
]

now=datetime.now()

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


# using an access token
g = Github(githubToken)

issues_since=datetime.now()-timedelta(days=30)

total_count = 0
triaged_count = 0
expected_total_time_to_triage = timedelta()
total_time_to_triage = timedelta()

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
        if is_triaged(first_label_events):
            total_time_to_triage += time_to_triage
            triaged_count += 1
            print('Issue %s created %s ago and triaged in %s' % (issue.html_url, humanize.naturaldelta(
                now - issue.created_at), humanize.naturaldelta(time_to_triage)))
        else:
            print('Issue %s created %s ago but still not triaged, assuming %s to triage' % (
                issue.html_url, humanize.naturaldelta(now - issue.created_at), humanize.naturaldelta(time_to_triage)))

average_days_to_triage = (total_time_to_triage / triaged_count).total_seconds() / ONE_DAY.total_seconds()
expected_average_days_to_triage = (expected_total_time_to_triage / total_count).total_seconds() / ONE_DAY.total_seconds()

output = json.dumps({
    'date': now.strftime('%Y-%m-%d'),
    'last_30days_total_issues': total_count,
    'last_30days_total_issues_triaged': triaged_count,
    'last_30days_average_days_to_triage': average_days_to_triage,
    'last_30days_expected_average_days_to_triage': expected_average_days_to_triage,
})

print("%d issues, %lf %% triaged, %.2lf days on average" % (total_count,
      (triaged_count * 100.0) / total_count, expected_average_days_to_triage))

print(output)
with DaprClient() as d:
    d.wait(60)
    filename = now.strftime('%Y/%m/%d') + '/last_30days_triage_metrics.json'
    resp = d.invoke_binding(
        binding_name='dapr-github-metrics-binding',
        operation='create',
        data=output,
        binding_metadata={
            'blobName': filename,
            'fileName': filename,
        })
    print(resp.json())
