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

from roles import replica


class Farm(object):
    def __init__(self, num_acceptors=2, num_leaders=1, num_replicas=5):
        self.num_acceptors = num_acceptors
        self.num_leaders = num_leaders
        self.num_replicas = num_replicas

        self.farm = {
            'replica': {},
            'leader': {},
            'acceptor': {},
        }

        # TODO(CGenie)
        for i in range(num_acceptors):
            name = 'acceptor_%d' % i
            self.farm['acceptor'][name] = {}

        # TODO(CGenie)
        for i in range(num_leaders):
            name = 'leader_%d' % i
            self.farm['leader'][name] = {}

        for i in range(num_replicas):
            name = 'replica_%d' % i
            self.farm['replica'][name] = replica.Replica.start(name)

    def get(self, role, name):
        return self.farm[role][name]

    def ask(self, role, name, message):
        """Ask specific role a message.

        This abstraction allows for role/network failure simulation.

        :param role:
        :param name:
        :param message:
        :return:
        """

        return self.get(role, name).ask(message)

    def ask_all(self, role, message):
        """Ask all roles a message.

        This abstraction allows for role/network failure simulation.

        :param role:
        :param name:
        :param message:
        :return:
        """

        return [r.ask(message) for r in self.farm[role].values()]

    def tell(self, role, name, message):
        """Tell specific role a message.

        This abstraction allows for role/network failure simulation.

        :param role:
        :param name:
        :param message:
        :return:
        """

        return self.get(role, name).tell(message)

    def tell_all(self, role, message):
        """Tell all roles a message.

        This abstraction allows for role/network failure simulation.

        :param role:
        :param name:
        :param message:
        :return:
        """

        return [r.tell(message) for r in self.farm[role].values()]
