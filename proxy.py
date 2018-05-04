import asynchat
import asyncore
import socket
import string

class proxy_server (asyncore.dispatcher):

    def __init__ (self, host, port, num):
        asyncore.dispatcher.__init__ (self)
        self.create_socket (socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.there = (host, port)
        here = ('', port + 8000)
        self.bind (here)
        self.listen (0)
        self.num = num
        self.i = 0

    def handle_accept (self):
#        if self.i < self.num:
#            print 'New connection'
#            self.i = self.i + 1
#            conn, addr = self.accept()
#            proxy_receiver (self, (conn, addr))
#        elif self.i >= self.num:
#            print '\n\n\n !!!!!!!!!!!!!! Rejecting connection %s !!!!!!!!!! \n\n\n' % self.i
#            conn, addr = self.socket.accept()
#            conn.close()
#            self.i = 0
        print 'New connection'
        conn, addr = self.accept()
        proxy_receiver (self, (conn, addr))

class proxy_sender (asynchat.async_chat):

    "Sends data to the server"

    def __init__ (self, receiver, address):
        asynchat.async_chat.__init__ (self)
        self.receiver = receiver
        self.set_terminator (None)
        self.create_socket (socket.AF_INET, socket.SOCK_STREAM)
        self.buffer = ''
        self.set_terminator ('')
        self.connect (address)

    def handle_connect (self):
        print 'Sender connected'

    def collect_incoming_data (self, data):
        self.buffer = self.buffer + data
        print '==> (%d) %s' % (self.id, repr(data))
        self.receiver.push (data)

    def found_terminator (self):
        data = self.buffer
        self.buffer = ''
        print '==> (%d) %s' % (self.id, repr(data))
        self.receiver.push (data + '')

    def handle_close (self):
        print "Closing Connection"
        if len( self.buffer ):
            self.found_terminator()

        self.receiver.close_when_done()
        self.close()

class proxy_receiver (asynchat.async_chat):

    "Receives data from the caller"

    channel_counter = 0

    def __init__ (self, server, (conn, addr)):
        asynchat.async_chat.__init__ (self, conn)
        self.set_terminator ('')
        self.server = server
        self.id = self.channel_counter
        self.channel_counter = self.channel_counter + 1
        self.sender = proxy_sender (self, server.there)
        self.sender.id = self.id
        self.buffer = ''
#        self.socket = ssl.wrap_socket(conn, server_side=True,
#                                      certfile='keycert.pem',
#                                      do_handshake_on_connect=False)
#        while True:
#            try:
#                self.socket.do_handshake()
#                break
#            except ssl.SSLError, err:
#                if err.args[0] == ssl.SSL_ERROR_WANT_READ:
#                    select.select([self.socket], [], [])
#                elif err.args[0] == ssl.SSL_ERROR_WANT_WRITE:
#                    select.select([], [self.socket], [])
#                else:
#                    raise
#        self.push("hello there!")

    def collect_incoming_data (self, data):
        import re
        print '<== (%d) %s' % (self.id, repr(data))
        #data = re.sub( r'\:8443', '', self.buffer )
        data = re.sub( r'localhost', self.server.there[0], data )

        self.buffer = self.buffer + data
        self.sender.push (data)

    def found_terminator (self):
        import re
        data = re.sub( r'\:8443', '', self.buffer )
        data = re.sub( r'localhost', self.server.there[0], data )
        self.buffer = ''
        print '<== (%d) %s' % (self.id, repr(data))
        self.sender.push (data + '')

    def handle_close (self):
        print "Closing Connection"
        if len( self.buffer ):
            self.found_terminator()

        self.sender.close_when_done()
        self.close()

if __name__ == '__main__':
    import sys
    import string
    if len(sys.argv) < 3:
        print 'Usage: %s <server-host> <server-port>' % sys.argv[0]
    else:
        ps = proxy_server (sys.argv[1], string.atoi (sys.argv[2]), string.atoi (sys.argv[3]))
        asyncore.loop()