import pykka

from pyxos.lib import state_machine


class Replica(pykka.ThreadingActor):
    def __init__(self, name):
        super(Replica, self).__init__()
        self.name = name
        self.machine = state_machine.StateMachine(name)

    def on_receive(self, message):
        print 'Replica', self.name, message
        command = message['command']

        if command == 'get':
            key = message['key']

            return self.machine.state.get(key)

        elif command == 'set':
            key = message['key']
            value = message['value']

            self.machine.op(key, value)
