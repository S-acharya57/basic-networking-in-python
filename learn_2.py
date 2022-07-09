import threading
import time

x = 8192

lock = threading.Lock()#allow or forbid us the resource 

def double():
	global x, lock
	lock.acquire()#getting the lock in a specific function
	while x< 163:
		x*=2
		print(x)
		time.sleep(1)
	print("Maximum")
	lock.release()#it releases the lock

def halve():
	global x, lock
	lock.acquire()
	while x>1:
		x/=2
		print(x)
		time.sleep(1)
	lock.release()

t1 = threading.Thread(target=halve)
t2= threading.Thread(target = double)

t1.start()
t2.start()
