from threading import Lock, Thread

x = 0   #free

def increment(lock):
	lock.acquire()
	global x
	x += 1
	lock.release()

def display(lock):
	lock.acquire()
	global x
	print("x = {0}".format(x))
	lock.release()

def thread_task(lock):
	for _ in range(100000):
		increment(lock)
	display(lock)
	


def main():
	lock_ = Lock()

	thread_pool = []
	for _ in range(5):
		t = Thread(target=thread_task, args=(lock_,))
		thread_pool.append(t)
	
	for i in thread_pool:
		i.start()

if __name__ == "__main__":
	main()
