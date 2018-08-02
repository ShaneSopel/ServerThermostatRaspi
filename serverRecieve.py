#This code is for the multicast receive servers
#Basically the Computers in your server room.
#It will receive the data from the raspi application
#It will then send back an ack message
#It will also shutdown your 
import os
import socket
import struct
import sys
import time

multicast_group = '239.0.0.1'
server_address = ('', 5007)

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

    print ('received from ', address, file=sys.stderr)

    result = float(data.decode())

    if result < 95:
        print('\033[1;32mTemperature is %s \nRoom is still safe\033[1;m' % result)

    if result > 95:
        print('\033[1;31mTemperature is %s \nRoom is NOT still safe\033[1;m' % result)
        print ('Shuting down in 5 seconds')
        time.sleep(5)
        os.system('shutdown -h now')
        break
 
    print ('sending acknowledgement to', address, file=sys.stderr)
    sock.sendto('Recieved temperature Message'.encode(), address)

    time.sleep(1)
