#!/usr/bin/env python

import pykka

from roles import replica


REPLICAS = []


def start_replicas():
    for i in range(5):
        r = replica.Replica.start(str(i))
        REPLICAS.append(r)


if __name__ == '__main__':
    start_replicas()

    ret = REPLICAS[0].ask({'command': 'get', 'key': 'x'}, timeout=3)
    print 'Replica returned', ret

    REPLICAS[0].tell({'command': 'set', 'key': 'x', 'value': '1'})
    ret = REPLICAS[0].ask({'command': 'get', 'key': 'x'}, timeout=3)
    print 'Replica returned', ret

    pykka.ActorRegistry.stop_all()