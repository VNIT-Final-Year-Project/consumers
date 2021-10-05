from Queueworker.queueWorker import Queueworker
import threading



queueWorker = Queueworker()

t1 = threading.Thread(target=queueWorker.consume)

t2 = threading.Thread(target=queueWorker.produce)



t3 = threading.Thread(target=queueWorker.calculate)
t4 = threading.Thread(target=queueWorker.calculate)
t5 = threading.Thread(target=queueWorker.calculate)
t6 = threading.Thread(target=queueWorker.calculate)
t7 = threading.Thread(target=queueWorker.calculate)
t8 = threading.Thread(target=queueWorker.calculate)

t2.start()
t1.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
