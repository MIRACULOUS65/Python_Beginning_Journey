import threading
import time

def worker(num):
    print(f"Worker {num}: starting")
    time.sleep(2)
    print(f"Worker {num}: finished")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()


# IT'S LIKE UPGRADED VERSION OF FOR LOOP KIND OF LIKE SYCHRONOUS PROGRAMMINGAND ASYNCHRONOUS PROGRAMMING WHERE IN SYNCHRONOUS PROGRAMMING, ONE TASK IS DONE THEN NEXT TASK STARTS AND IN ASYNCHRONOUS PROGRAMMING, MULTIPLE TASKS CAN RUN SIMULTANEOUSLY.