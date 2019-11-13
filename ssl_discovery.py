#!/usr/bin/env python

import os
import re
import json

opsys = os.uname()

if (opsys[0] == "Linux"):
  apache_path = "/etc/apache2/sites-enabled/"
  nginx_path = "/etc/nignx/"
elif (opsys[0] == "FreeBSD"):
  apache_path = "/usr/local/etc/apache24/extra/"
  nginx_path = "/usr/local/nginx/conf/"

#create structure for discovered data
discovery = {"data":[]}
portList = []

#look for apache config files
if os.path.exists(apache_path):
  for fname in os.listdir(apache_path):
    with open("%s%s" % (apache_path, fname), "r") as fhandle:
      for line in fhandle:
        pm = re.match("<VirtualHost \*\:(\d+)>", line)
        if pm:
          if pm.group(1) not in portList:
            portList.append(pm.group(1))
#else:
#  print("no apache files found")

#look for nginx conf files
if os.path.exists(nginx_path):
  for fname in os.listdir(nginx_path):
    if fname.endswith(".conf"):
      with open("%s%s" % (nginx_path, fname), "r") as fhandle:
        for line in fhandle:
          pm = re.match("\s+listen\s+.*:(\d+) default.*", line)
          if pm:
            if pm.group(1) not in portList:
              portList.append(pm.group(1))
#else:
#  print("no nginx file found")
#add discovered ssl ports to json object
for port in portList:
  if port != "80":
    discovery["data"].append({"{#SSLPORT}":port})

print(json.dumps(discovery))