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


# Command is key:value
class StateMachine(object):
    def __init__(self, name):
        self.slot_num = 0
        self.state = {}
        self.name = name
        self.ops = self._read_file_ops()

        for key, value in self.ops:
            self.op(key, value)

    def _read_file_ops(self):
        ret = []

        try:
            with open(self.name) as f:
                for line in f:
                    ret.append(self._read_file_op(line))
        except IOError:
            pass

        return ret

    def _read_file_op(self, line):
        slot_num, key, value = line.strip().split('|')

        self.slot_num = int(slot_num)

        return (key, value)

    def _save_file_op(self, key, value):
        with open(self.name, 'a') as f:
            f.write('%s|%s|%s\n' % (self.slot_num, key, value))

    def op(self, key, value):
        self.state[key] = value
        self.ops.append((key, value))
        self._save_file_op(key, value)
