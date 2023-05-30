import threading
import time		

mutex = threading.Semaphore(1)

x = 0

def increment(y):	
	mutex.acquire()   #check semaphore value
	global x			
	for _ in range(y):
		x += 1

		mutex.release()

def display():
	mutex.acquire()   #check semaphore value
	global x
	print("x = {0}, current_thread_id = {1}".format(x, threading.current_thread().ident))
	mutex.release()

def thread_task():
	increment(10000)
	display()
	
def main():		
	thread_pool = []

	for _ in range(5):
		t = threading.Thread(target = thread_task)
		thread_pool.append(t)

	for i in thread_pool:
		i.start()

if __name__ == "__main__":
	main()














# A semaphore maintains a count that represents the number of threads that are currently allowed 
# to access the shared resource. When a thread wants to access the shared resource, 
# it must first acquire the semaphore. If the count is greater than 0, the thread is 
# allowed to access the resource and the count is decremented. If the count is 0, the thread is
# blocked until another thread releases the semaphore, which increments the count and 
# allows one of the blocked threads to proceed.

# In this program, a Semaphore object mutex is created with an initial value of 1, 
# which means that only one thread at a time can access the shared resource. 
# When a thread calls the acquire() method on the mutex semaphore, 
# it tries to acquire the semaphore. 
# If the count is 0 (i.e., the semaphore is already held by another thread), 
# the calling thread will block until the semaphore becomes available. 
# Once the semaphore is available, the calling thread acquires the semaphore 
# and can proceed with accessing the protected resource. 
# When the thread is finished with accessing the resource, 
# it must release the semaphore by calling the release() method on the semaphore object. 
# This increments the count and allows another thread to acquire the semaphore 
# and access theshared resource.