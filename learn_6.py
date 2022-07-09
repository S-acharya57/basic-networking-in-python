#sockets
#lower level of connections is dealt in this
import socket

#internet or unix socket??
#what protocol? TCP-> slow but reliable or UDP-> fast but might have losses?
#which IP? 
#which port? 

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#AF_NET-> internet socket, SOCK_STREAM-> TCP?

s.bind(('127.0.0.1', 55555))#IP and port
s.listen()

while True:
	client, address= s.accept()
	print("Connected to {}".format(address))
	client.send("You are connected".encode())
	client.close()

