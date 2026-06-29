import threading
import time

def worker(num):
    print(f"thread {num}: starting ")
    time.sleep(2) #stimulate some work, wait for 2 seconds
    print(f"thread {num}: finishing ")

threads=[]
for i in range(3):
    thread = threading.Thread(target=worker,args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join() #  wait for all threads to finish

print("all threads completed.")
