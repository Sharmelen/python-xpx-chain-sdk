"""
    responses
    =========

    Mocked response data for the .

    License
    -------

    Copyright 2019 NEM

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import json
import os

DIR = os.path.dirname(os.path.realpath(__file__))
DATADIR = os.path.join(DIR, 'data')
ENDPOINT = os.environ.get('NIS2_ENDPOINT', 'http://localhost:3000')


def load_response(name):
    with open(os.path.join(DATADIR, name)) as f:
        data = json.load(f)
        data['content'] = data['content'].encode('utf8')
        return data


BLOCK_INFO = {
    'Ok': load_response('block_info.json'),
}

MOSAIC_INFO = {
    'Ok': load_response('mosaic_info.json'),
}

NAMESPACE_INFO = {
    'nem': load_response('namespace.json'),
}

NAMESPACE_NAMES = {
    'nem': load_response('namespace_names.json'),
}

NETWORK_TYPE = {
    'MIJIN_TEST': load_response('network.json'),
}
