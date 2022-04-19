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
import re
import sys
import humanize

from datetime import datetime, timedelta
from string import Template

from github import Github


githubToken = os.getenv("GITHUB_TOKEN")

my_repos=[
    'dapr',
    'cli',
    'components-contrib']

expected_triage_labels=[
    ('P0', 'P1', 'P2', 'P3'),
    ('size/xs', 'size/s', 'size/m', 'size/l', 'size/xl'),
    ('pinned', 'triaged/resolved')
]


# using an access token
g = Github(githubToken)

# discover milestone project
issues = [i for i in g.get_repo("dapr/dapr").get_issues(labels=['kind/bug'], since=(datetime.now()-timedelta(days=30)))]

def is_triaged(label_events):
    for expected_label_set in expected_triage_labels:
        if True not in [l.lower() in label_events for l in expected_label_set]:
            return False
    return True

def get_triaged_time(label_events):
    timestamps=[]
    for expected_label_set in expected_triage_labels:
        for label in expected_label_set:
            if label in label_events:
                timestamps = timestamps + [label_events[label]]
    if len(timestamps) == 0:
        return datetime.now()
    return max(timestamps)

total_count = len(issues)
triaged_count = 0
total_time_to_triage = timedelta()

for issue in issues:
    events = sorted(issue.get_events(), key=lambda e:str(e.created_at))
    # Dictionary of the latest time 
    first_label_events = dict()
    for event in events:
        if event.event == 'labeled':
            canonical_label = event.label.name.lower()
            if canonical_label not in first_label_events:
                first_label_events[canonical_label] = event.created_at
    if is_triaged(first_label_events):
        triaged_time = get_triaged_time(first_label_events)
        time_to_triage = triaged_time - issue.created_at
        total_time_to_triage += time_to_triage
        triaged_count += 1
        print('Issue ' + issue.html_url + ' triaged after ' + humanize.naturaldelta(time_to_triage))
    else:
        print('Issue ' + issue.html_url + ' is not triaged')

print("%d issues, %lf pct triaged on average after %s" % (total_count, (triaged_count * 100.0) / total_count, humanize.naturaltime(total_time_to_triage / triaged_count)))
