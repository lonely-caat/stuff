from ldap3 import Server, Connection, ALL, SASL, KERBEROS
import datetime

server = Server('ldap.llnw.com', get_info=ALL)
con = Connection(server)
services = {'servicenow': 'limon2.rest.dev','servicenow_stage':'limon2.rest.uat',
            'servicenow_prod': 'limon.te.prod.b',
            'confluence': 'limonconfluenceread',
            'zabbix_qa': 'zabbix-api-limon-qa',
            'zabbix_dba_qa': 'zabbix-api-limon2', 'email': 'limon_noreply',
            }


def find_expiration():
    expiration = []
    try:
        con.bind()
        for service, user in services.items():
            if con.search('cn={0},ou=Applications,dc=llnw,dc=com'.format(user), '(objectclass=*)',
                       attributes=['llnwUnixPasswordChangedTime']):
                expiration.append(con.response[0]['attributes'])

        print(expiration)


    except Exception:
        return 'Cannot connect to LDAP server'

    now = datetime.datetime.now()


find_expiration()