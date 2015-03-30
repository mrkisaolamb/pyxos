#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import six
import uwsgi

from roles.scout import Scout


def mule_loop():
    while True:
        six.print_("mule: Waiting for messages... yawn.")
        message = uwsgi.mule_get_msg()
        Scout(message)

if __name__ == '__main__':
    mule_loop()
