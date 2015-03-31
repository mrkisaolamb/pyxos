#!/bin/bash

uwsgi --http :9090 --wsgi-file main.py --socket :3031 --mule=roles/leader.py
