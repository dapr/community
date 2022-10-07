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

import json

from dapr.clients import DaprClient


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
    
    gh_env_file = os.getenv('GITHUB_ENV')

    with open(gh_env_file, "a") as myfile:
        for k, v in data['metrics'].items():
            myfile.write("DAPR_%s=%s\n" % (k.upper(), v))