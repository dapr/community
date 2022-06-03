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

import json

from dapr.clients import DaprClient


def alert(dapr_client, message):
    dapr_client.invoke_binding(
        binding_name='dapr-discord-binding',
        operation='post',
        data=json.dumps({'content': message}),
        binding_metadata={
            'Content-Type': 'application/json',
            })

with DaprClient() as d:
    d.wait(60)
    filename ='github_issues_metrics.json'
    resp = d.invoke_binding(
        binding_name='dapr-github-metrics-binding',
        operation='get',
        data='',
        binding_metadata={
            'blobName': filename,
            'fileName': filename,
        })
    print(resp.text())

    data = json.loads(resp.text())
    
    alert_time_to_triage_bugs = '<#889972784216805397> %d%% of bugs created in last 30 days are triaged within 5 days.' % (data['metrics']['last_30days_percentage_bugs_triaged_within_5_days'])
    alert(d, alert_time_to_triage_bugs)

    alert_bugs_not_triaged_message = '<#889972784216805397> Detected bugs that are not triaged:'
    for bug in data['not_triaged_bugs']:
        alert_bugs_not_triaged_message += '\n%s was created %s ago.' % (bug['url'], bug['age'])
    alert(d, alert_bugs_not_triaged_message)