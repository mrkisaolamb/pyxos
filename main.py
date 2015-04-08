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

from pyxos import farm


if __name__ == '__main__':
    f = farm.Farm()

    ret = f.get('replica', 'replica_1').ask({'command': 'get', 'key': 'x'},
                                            timeout=3)
    six.print_('Replica returned', ret)

    f.get('replica', 'replica_1').tell({
        'command': 'set', 'key': 'x', 'value': '1'
    })
    ret = f.get('replica', 'replica_1').ask({'command': 'get', 'key': 'x'},
                                            timeout=3)
    six.print_('Replica returned', ret)

    pykka.ActorRegistry.stop_all()
