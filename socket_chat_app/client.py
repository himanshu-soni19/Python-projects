import socket
port = 3000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
CHUNK = 65535
# instead of explicitly binding socket, I will let os do it
# ephemeral ports
# os will bind this for us
hostname = '127.0.0.1'
while True:
    s.connect((hostname, port))
    message = input("Type message: ")
    data = message.encode('ascii')
    s.send(data)
    # data recieve
    data = s.recv(CHUNK)
    text = data.decode('ascii')
    print(f"Himanshu: {text}")
