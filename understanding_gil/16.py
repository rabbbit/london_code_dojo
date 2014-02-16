from threading import Thread
import time

def countdown(n):
	while n > 0:
		n -= 1

COUNT = 50000000
NO = 16


threads = []
for c in range(NO):
	threads.append(Thread(target=countdown, args=(COUNT//NO,)))

start = time.time()

for t in threads:
	t.start()

for t in threads:
	t.join()
	
print time.time() - start

