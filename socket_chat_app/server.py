import socket
CHUNK = 65535 # recieve atmost these bytes of data at once
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # create a socket object
# syntax => socket.socket(family, type)
# AF_NEt : family of ipv4 ip address
# SOCK_STREAM: TCP, SOCK_DGRAM: UDP

# some ip address that the server will listen to when message comes
hostname = '127.0.0.1'  # ip address of local machine, same for everyone
# aka home, there is no place like 127.0.0.1

s.bind((hostname, port))  # bind the socket with this host machine and on port 3000
print(f"server is live on {s.getsockname()}")


# run this server infinitely,till I stop manually
while True:  # infinite loop
    data, clientAdd = s.recvfrom(CHUNK)
    message = data.decode('ascii')  # data by default travels in bytes
    print(f"Saket: {message}")
    message_send = input("Reply: ")
    data = message_send.encode('ascii')
    # send data to the ip add that sent me the data
    s.sendto(data, clientAdd)
