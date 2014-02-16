from threading import Thread
import time

def countdown(n):
	while n > 0:
		n -= 1

COUNTS = [500000, 5000000, 50000000, 500000000]

NO = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 5096]

for count in COUNTS:

	start = time.time()
	countdown(count)
	print 'COUNT %10s ' % count, 'NO %3s' % '0', time.time() - start

	for no_threads in NO:
		threads = []
		for c in range(no_threads):
			threads.append(Thread(target=countdown, args=(count//no_threads,)))

		start = time.time()

		for t in threads:
			t.start()

		for t in threads:
			t.join()
			
		print 'COUNT %10s ' % count, 'NO %3s' % no_threads, time.time() - start

