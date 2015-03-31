#!/usr/bin/env python

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import pykka
import six

from roles import replica


REPLICAS = []


def start_replicas():
    for i in range(5):
        r = replica.Replica.start(str(i))
        REPLICAS.append(r)


if __name__ == '__main__':
    start_replicas()

    ret = REPLICAS[0].ask({'command': 'get', 'key': 'x'}, timeout=3)
    six.print_('Replica returned', ret)

    REPLICAS[0].tell({'command': 'set', 'key': 'x', 'value': '1'})
    ret = REPLICAS[0].ask({'command': 'get', 'key': 'x'}, timeout=3)
    six.print_('Replica returned', ret)

    pykka.ActorRegistry.stop_all()
