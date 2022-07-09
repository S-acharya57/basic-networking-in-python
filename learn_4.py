import threading

event =threading.Event()

def func():
	print("wait time")
	event.wait()
	print("permorning now")

t1= threading.Thread(target = func)
t1.start()

x=input("Wanna trigger it?")
if x=="y":
	event.set()