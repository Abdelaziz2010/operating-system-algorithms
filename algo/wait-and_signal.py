from random import random
import threading
import time

result = 0
result_available = threading.Event()

def background_calculation():
    time.sleep(2)

    global result
    result = 42
    result_available.set()

    time.sleep(2)

def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

    result_available.wait()

    print('The result is', result)

if __name__ == '__main__':
    main()