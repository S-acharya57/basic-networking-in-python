import socket
import threading

nickname = input("Choose a nickname")

client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 4000))

def receive():
	while True:
		try:
			message = client.recv(1024).decode('ascii')
			if messsage =="NICK":
				client.send(nickname.enode('ascii'))
			else:
				print(message)
		except:
			print("An error")
			client.close()
			break

def write():
	while True:
		message = f'{nickname}: {input("")}'#constant input 
		client.send(message.encode('ascii'))
receive_thread  =threading.Thread(target = receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()