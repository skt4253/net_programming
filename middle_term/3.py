import socket
import binascii
import sys

ip = "220.69.189.125"
port = 443

print(socket.getfqdn(ip))
print(socket.getservbyport(port))
print(socket.getservbyport(port) + "://" + socket.getfqdn(ip))
print(socket.inet_aton(ip))