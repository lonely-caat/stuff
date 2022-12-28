import os

with open('/var/www/ui/storage/app/device_group_devices.json', 'r') as groups:
    content = groups.read()

dic= eval(content)

hosts_set = set(x for x in dic.keys())
hosts = list(hosts_set)

# call(["ls", "-l"])
os.chdir("/var/www/ui/")
for host in hosts:
    os.system("php artisan metrics:generate:dumb --user=mbilichenko --triggerId=666 --eventId=667 --ticketId=668 --ticketStatus=CLOSED --duration=669--host={0}".format(host))
