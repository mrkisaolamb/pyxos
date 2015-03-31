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
from pyxos import farm


@mock.patch('pyxos.lib.state_machine.open', create=True)
class TestFarm(unittest.TestCase):
    def tearDown(self):
        pykka.ActorRegistry.stop_all()

    def test_farm_initialization(self, mopen):
        mopen.return_value = mock.MagicMock(spec=file)

        f = farm.Farm(num_acceptors=3, num_replicas=2, num_leaders=1)
        self.assertItemsEqual(
            f.farm['acceptor'].keys(),
            ['acceptor_0', 'acceptor_1', 'acceptor_2']
        )
        self.assertItemsEqual(
            f.farm['leader'].keys(),
            ['leader_0']
        )
        self.assertItemsEqual(
            f.farm['replica'].keys(),
            ['replica_0', 'replica_1']
        )

    def test_farm_get(self, mopen):
        mopen.return_value = mock.MagicMock(spec=file)

        f = farm.Farm(num_acceptors=3, num_replicas=2, num_leaders=1)
        self.assertEqual(
            f.get('replica', 'replica_1').ask({'command': 'name'}),
            'replica_1'
        )

    def test_farm_ask(self, mopen):
        mopen.return_value = mock.MagicMock(spec=file)

        f = farm.Farm(num_acceptors=3, num_replicas=2, num_leaders=1)
        self.assertEqual(
            f.ask('replica', 'replica_1', {'command': 'name'}),
            'replica_1'
        )
        self.assertItemsEqual(
            f.ask_all('replica', {'command': 'name'}),
            ['replica_0', 'replica_1']
        )
