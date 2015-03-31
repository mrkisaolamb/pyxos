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

from pyxos.lib import state_machine


@mock.patch('pyxos.lib.state_machine.open', create=True)
class TestStateMachine(unittest.TestCase):
    def test_machine_init(self, mopen):
        mopen.return_value = mock.MagicMock(spec=file)

        machine = state_machine.StateMachine('x')
        self.assertDictEqual(machine.state, {})
        self.assertListEqual(machine.ops, [])

    def test_machine_op(self, mopen):
        mopen.return_value = mock.MagicMock(spec=file)

        machine = state_machine.StateMachine('x')
        machine.op('x', 'y')
        self.assertDictEqual(machine.state, {'x': 'y'})
        self.assertListEqual(machine.ops, [('x', 'y')])

        machine.op('x', 'z')
        self.assertDictEqual(machine.state, {'x': 'z'})
        self.assertListEqual(machine.ops, [('x', 'y'), ('x', 'z')])
