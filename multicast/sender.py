# -*- coding: utf-8 -*-
import socket
import struct
import argparse

parser = argparse.ArgumentParser(description = 'Trabalho de Sistemas Distribuídos. (Multicast para executar cálculo de expressão matemática)')
parser.add_argument('--e', action = 'store', dest = 'expressao',
                           default = '2+2', required = True,
                           help = 'A expressão matemática que será calculada pelo multicast.')
arguments = parser.parse_args()

message = arguments.expressao + ' - client'
multicast_group = ('224.3.29.71', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(5)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    # Send data to the multicast group
    print('sending "%s"' % message)
    sent = sock.sendto(message.encode(), multicast_group)

    # Look for responses from all recipients
    while True:
        print('waiting to receive')
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print('timed out, no more responses')
            break
        else:
            print('received "%s" from %s' % (data, server))

finally:
    print('closing socket')
    sock.close()