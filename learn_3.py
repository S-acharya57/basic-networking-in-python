import threading
import time

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
	print("{} is trying to access".format(thread_number))
	semaphore.acquire()
	print("{} was granted access".format(thread_number))
	time.sleep(5)
	print("{} is releasing the access".format(thread_number))
	semaphore.release()

for thread_number in range(1, 11):
	t=threading.Thread(target=access, args =(thread_number, ))
	t.start()
	time.sleep(5)