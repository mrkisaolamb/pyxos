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
