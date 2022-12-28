import subprocess
from paramiko import SSHClient
import getpass
from progress.bar import Bar

# subprocess.call('kill $(lsof -t -i:2216)', shell=True)

zero = 'zabbix_sender -vv -s zabbix-main01.dev.phx7.llnw.net -z zabbix-proxy01.dev.phx7.llnw.net -k sl.foundry.v2 -o "0"'
one = 'zabbix_sender -vv -s zabbix-main01.dev.phx7.llnw.net -z zabbix-proxy01.dev.phx7.llnw.net -k sl.foundry.v2 -o "1"'
port = 2216
zabbix = 'zabbix-proxy01.dev.phx7.llnw.net'

def gen_events_stateless(username,password, enable=True):

    #kill anything that resides on that port already
    subprocess.call('kill $(lsof -t -i:2216)', shell=True)

    #lay out a tunnel through jumphost
    subprocess.call('ssh -f -N -L {0}:{1}:22 {2}@dingo.llnw.com'.format(port,zabbix,username), shell=True)

    ssh = SSHClient()
    ssh.load_system_host_keys()
    ssh.connect('127.0.0.1',2216, username,password)

    #first send a few fake signals
    bar = Bar('Please wait:3', fill=':3',max=10)
    for element in range(10):
        ssh.exec_command(zero)
        from time import sleep;sleep(1)
        bar.next()
    bar.finish()

    if enable:
        ssh.exec_command(one)
        print('Events should"ve been generated')
    else:
        print('The events have been disabled')


if __name__ == '__main__':
    import sys
    import os
    os_user = os.getenv("USER")
    # ensure 2/3 compatibility
    try: input = raw_input
    except NameError: pass



    if len(sys.argv) > 1:
        print('Usage: %s <server-host> <server-port>' % sys.argv[0], sys.argv[1])
    else:
        gen_events_stateless(username=input('Enter your LDAP username or hit "Enter" to use "{0}" \n'.format(os_user)) or os_user,
                   password=getpass.getpass(prompt='LDAP Password'))