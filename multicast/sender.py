# chat server using multicast
# python fork of the original ruby implementation
# http://tx.pignata.com/2012/11/multicast-in-ruby-building-a-peer-to-peer-chat-system.html
# send.py
# usage : $ python send.py message

from distutils.version import LooseVersion, StrictVersion
from platform import python_version
import socket
import struct
import sys

message = sys.argv[1] if len(sys.argv) > 1 else 'message via multicast'

multicast_addr = '224.0.0.1'
port = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
if LooseVersion(python_version()) >= LooseVersion("3.0.0"):
	sock.sendto(bytes(sys.argv[1], 'UTF-8'), (multicast_addr, port))
	data, address = sock.recvfrom(1024)
	print('Mensagem: %s de %s' % (bytes(data, 'UTF-8'), address))
else:
	sock.sendto(sys.argv[1], (multicast_addr, port))
	data, address = sock.recvfrom(1024)
	print('Mensagem: %s de %s' % (data, address))
sock.close()