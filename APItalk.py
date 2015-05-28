__author__ = 'Vlasev'

import json, requests

payload = {'v': '1', 'format': 'json', 't.p': '36280', 't.k': 'iIrHzCDrG5I', 'userip': '205.250.230.105', 'action': 'employers', 'useragent': 'Windows NT 6.1'}
req = requests.get("http://api.glassdoor.com/api/api.htm", params=payload)
print(req.url)
print(req)
