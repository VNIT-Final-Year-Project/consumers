from Queueworker.queueWorker import Queueworker
import threading


queueWorker = Queueworker()

t1 = threading.Thread(target=queueWorker.consume)

t2 = threading.Thread(target=queueWorker.produce)

t3 = threading.Thread(target=queueWorker.calculate)

t2.start()
t1.start()
t3.start()
t1.join()
t2.join()
t3.join()
