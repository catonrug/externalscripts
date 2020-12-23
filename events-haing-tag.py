#!/usr/bin/env python3.6

import sys
from datetime import datetime
import time
import logging
from pyzabbix import ZabbixAPI
import pprint
import re

sys.path.insert(0,'/var/lib/zabbix')
import config
ZABBIX_SERVER = config.url
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login(config.username, config.password)


# Get timestamps from 30 days back
start_time = int(time.time()) - 300000

# get tagged events
#r=zapi.event.get(time_from = start_time, tags=[{'tag': 'autoclose_alert', 'value': '1', 'operator': 0}], output = ['eventid'])
r=zapi.problem.get(time_from = start_time, tags=[{'tag': 'autoclose_alert', 'value': '1', 'operator': 0}], output = ['eventid'])

# print ray array
print (r)

event_ids = [e['eventid'] for e in r]

print (event_ids)

events_closed = zapi.event.acknowledge(eventids = event_ids, action = '1')

print (events_closed)

