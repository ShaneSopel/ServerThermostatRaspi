import os
import socket
import struct
import sys
import time

multicast_group = '239.0.0.1'
server_address = ('', 5007)

# def to convert bytes to ints for data from thermostat
def bytes_to_int(bytes):
    result = 0

    for b in bytes:
        result = result * 256 + int(b)

    return result

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)
# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:
    print ('\nwaiting to receive message', file=sys.stderr)
    data, address = sock.recvfrom(1024)
    
    print ('received %s bytes from %s' % (len(data), address), file=sys.stderr)
    print (data.decode(), file=sys.stderr)
    
    result = bytes_to_int(data)

    if result > 70:
    	os.system('shutdown -h now')
    break
   
    print ('sending acknowledgement to', address, file=sys.stderr)
    sock.sendto('Recieved temperature Message'.encode(), address)

    time.sleep(1)
