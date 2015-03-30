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
