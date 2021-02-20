import socket
server = "127.0.0.2"
port = 1450
request_string = "127.0.0.1"
receive_buffer_size = 4096
mysocket = socket.socket()
mysocket.connect(server, port)
mysocket.send(request_string)
response_string = mysocket.recv(receive_buffer_size)
mysocket.close
print(response_string)
