#!/bin/python
"""
Shows a list of all current issues (AKA tripped triggers)
"""

import os
import json
import string
from pyzabbix import ZabbixAPI

#import credentials from external file
import sys
sys.path.insert(0,'/var/lib/zabbix')
import config

# The hostname at which the Zabbix web interface is available
ZABBIX_SERVER = config.url

zapi = ZabbixAPI(ZABBIX_SERVER)

# Login to the Zabbix API
zapi.login(config.username, config.password)

# define the API call from
# https://www.zabbix.com/documentation/3.4/manual/api/reference/maintenance/create

# define the methon
#def create_maintenance(zbx, request):
result=zapi.item.get(output='extend',
        hostids='10084',
	search={'key_':'system'},
        sortfield='name')
print result
# execute
#create_maintenance(zapi, request)
