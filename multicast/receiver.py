# -*- coding: utf-8 -*-
import socket
import struct
import sys
import time

multicast_group = '224.3.29.71'
server_address = ('', 10000)

multicast_group_servers = ('224.0.0.1', 10001)
my_host = socket.gethostbyname(socket.gethostname())
bind_addr = '0.0.0.0'
network_ips = {'10.10.10.1':[1,False], '10.10.10.2':[2,False], '10.10.10.3':[3,False], '10.10.10.4':[4,False]}

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

while True:
	print('\nwaiting to receive message BY CLIENT')
	data, address = sock.recvfrom(1024)
	network_ips = {'10.10.10.1':[1,False], '10.10.10.2':[2,False], '10.10.10.3':[3,False], '10.10.10.4':[4,False]}

	print('received %s bytes from %s' % (len(data), address))
	print(data.replace(b" - client", b""))

	# requisição vinda do cliente
	if(data.find(b"client") != -1):
		data = data.replace(b" - client", b"")
		network_ips = {'10.10.10.1':[1,False], '10.10.10.2':[2,False], '10.10.10.3':[3,False], '10.10.10.4':[4,False]}
		# Create the datagram socket
		sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

		# Set a timeout so the socket does not block indefinitely when trying
		# to receive data.
		sock2.settimeout(3)

		# Set the time-to-live for messages to 1 so they do not go past the
		# local network segment.
		ttl = struct.pack('b', 1)
		sock2.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

		try:
			# Bind to the server address
			sock2.bind((bind_addr, 10001))
			# Tell the operating system to add the socket to the multicast group2
			# on all interfaces.
			group2 = socket.inet_aton('224.0.0.1')
			mreq2 = struct.pack('4sL', group2, socket.INADDR_ANY)
			sock2.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq2)
			# Send data to the multicast group2
			print('sending HOST "%s"' % my_host)
			time.sleep(1)
			sent = sock2.sendto(str(my_host).encode('UTF-8'), multicast_group_servers)
			# Look for responses from all recipients
			while True:
				print('waiting to receive HOST')
				try:
					data2, server2 = sock2.recvfrom(1024)
				except socket.timeout:
					print('timed out, no more responses')
					break
				else:
					print('received HOST "%s" from %s' % (data2, server2))
					print(server2[0])
					network_ips[server2[0]] = [network_ips[server2[0]][0],True]
		finally:
			print('closing socket HOST')
			sock2.close()

		menor = -1
		ip = ''
		for i in network_ips:
			if(network_ips[i][1] and (menor == -1 or menor>network_ips[i][0])):
				menor = network_ips[i][0]
				ip = i
		
		print(network_ips)
		if(my_host == ip):
			# calculando expressao matematica recebida
			# solicita a expressão do usuario
			# valor = input("Digite uma expressão: \n")
			# cria uma variavel com o resultado da expressão
			valorint = eval(data)
			# imprime algumas linhas coisa de desing...
			print("Processando......")
			print("---------------------")
			# imprime a expressão no formato string, uma caractere '=' e o resultado
			print(data,"=",valorint)
			# mais design ...
			print("---------------------")
			print('sending acknowledgement to', address[0])
			sock.sendto(str(str(data) + " = " + str(valorint)).encode(), address)
		network_ips = {'10.10.10.1':[1,False], '10.10.10.2':[2,False], '10.10.10.3':[3,False], '10.10.10.4':[4,False]}
		# print(network_ips)
		# print('quem vai responder sera: ', ip)
		# print('sending acknowledgement to', address[0])
		# sock.sendto(b'ack', address)