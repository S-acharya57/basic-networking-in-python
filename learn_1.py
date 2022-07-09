import threading 

def hello():
	for i in range(10):
		print("Hello world")

def fun1():
	for i in range(10):
		print(i)

#use this function
tl = threading.Thread(target = fun1)
t2 = threading.Thread(target = hello)
tl.start()
t2.start()

print("Sajjan")
