#Daemon threads
#that runs in the background and not stop the main thread to run or exit
import threading
import time

path = "text.txt"
text=""

def read_file():
	global path, text
	while True:
		with open("text.txt", "r") as f:
			text = f.read()
		time.sleep(1)

def print_loop():
	for x in range (5):
		print(text)
		time.sleep(1)

t1 = threading.Thread(target = read_file, daemon=True)
t2 = threading.Thread(target = print_loop)

t1.start()
t2.start()
