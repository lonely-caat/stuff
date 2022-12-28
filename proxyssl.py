#!/usr/bin/python

import socket
from multiprocessing import Process
import ssl
import select
import re

RUN_PORT = 8888
TARGET_HOST = ''
#TARGET_HOST = 
__keep_alive = '\r\nProxy-Connection: Keep-Alive'
PROXY_CONNECT = 'CONNECT {0}:443 HTTP/1.1\r\nHost: {0}:443{1}\r\n\r\n'.format(TARGET_HOST, __keep_alive)
PROXY_HOST = 'tnproxy.phx2.llnw.com'
PROXY_PORT = 

HOSTNAME = socket.gethostbyaddr(socket.gethostname())[0]
if 'localhost' in HOSTNAME:
    HOSTNAME = 'localhost'


def client_thread(cl_sock, proxy_sock):
    rl = True
    try:
        while rl:
            rl, wl, xl = select.select([cl_sock, proxy_sock], [], [], 160)

            if cl_sock in rl:
                _tmp_data = cl_sock.recv(16384)
                if not _tmp_data:
                    break
                in_data = _tmp_data
                print('\r\n>> Incoming DATA len[{0}] \r\n {1}'.format(len(in_data), in_data))
                proxy_sock.send(fix_request(in_data))

            elif proxy_sock in rl:
                _tmp_data = proxy_sock.recv(16384)
                if not _tmp_data:
                    break
                out_data = _tmp_data
                print('\r\n>> Outgoing DATA len[{0}] \r\n {1}'.format(len(out_data), out_data))
                cl_sock.send(fix_request(out_data))
    except Exception:
        raise
    finally:
        proxy_sock.close()
        cl_sock.close()


def proxy_connect():
    proxy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_sock.connect((PROXY_HOST, PROXY_PORT))
    proxy_sock.send(PROXY_CONNECT)
    print(proxy_sock.recv(1024) + '\r\n')
    proxy_sock = ssl.wrap_socket(proxy_sock, do_handshake_on_connect=False)
    proxy_sock.do_handshake()
    return proxy_sock


def direct_connect():
    proxy_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    proxy_sock.connect((TARGET_HOST, 443))
    print('Connected to {0}'.format(TARGET_HOST))
    proxy_sock = ssl.wrap_socket(proxy_sock, do_handshake_on_connect=False)
    proxy_sock.do_handshake()
    return proxy_sock


def fix_request(data):
    if re.search(r'{0}'.format(HOSTNAME), data):
        data = re.sub(r'http://{0}:{1}/'.format(HOSTNAME, RUN_PORT), "https://{0}/".format(TARGET_HOST), data)
        data = re.sub(r'{0}:{1}'.format(HOSTNAME, RUN_PORT), "{0}".format(TARGET_HOST), data)
    elif re.search(r'{0}'.format(TARGET_HOST), data):
        data = re.sub(r'https://{0}/'.format(TARGET_HOST), "http://{0}:{1}/".format(HOSTNAME, RUN_PORT), data)
        data = re.sub(r'{0}'.format(TARGET_HOST), "{0}:{1}".format(HOSTNAME, RUN_PORT), data)
        data = re.sub(r';(S|s)ecure;', ';', data)
    return data


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('', RUN_PORT))
    print('Server started on port:{0}'.format(RUN_PORT))
    threads = []
    while True:
        server.listen(5)
        conn, addr = server.accept()
        print('Accepted connection from {0}'.format(addr))
        clinet_th = Process(target=client_thread, args=(conn, proxy_connect()))
        clinet_th.daemon = True
        clinet_th.start()
        threads.append(clinet_th)


if __name__ == '__main__':
    main()
