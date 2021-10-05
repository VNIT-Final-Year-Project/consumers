from Queueworker.queueWorker import Queueworker
import threading


queueWorker = Queueworker()

t1 = threading.Thread(target=queueWorker.consume)

t2 = threading.Thread(target=queueWorker.produce)

t3 = threading.Thread(target=queueWorker.calculate)
t4 = threading.Thread(target=queueWorker.calculate)
t5 = threading.Thread(target=queueWorker.calculate)

t2.start()
t1.start()
t3.start()
t4.start()
t5.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
