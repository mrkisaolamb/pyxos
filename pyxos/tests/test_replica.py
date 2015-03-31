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

import mock
import unittest

import pykka
from pyxos.roles import replica


@mock.patch('pyxos.lib.state_machine.open', create=True)
class TestReplica(unittest.TestCase):
    def tearDown(self):
        pykka.ActorRegistry.stop_all()

    def test_replica_message_get(self, mopen):
        mopen.return_value = mock.MagicMock(spec=file)

        r = replica.Replica.start('x')
        ret = r.ask({'command': 'get', 'key': 'x'}, timeout=1)
        self.assertIsNone(ret)

    def test_replica_message_set(self, mopen):
        mopen.return_value = mock.MagicMock(spec=file)

        r = replica.Replica.start('x')
        r.tell({'command': 'set', 'key': 'x', 'value': 'y'})
        ret = r.ask({'command': 'get', 'key': 'x'}, timeout=1)
        self.assertEqual(ret, 'y')
