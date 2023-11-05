from queue_LL import *

q1 = QueueUsingLL()
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
print(q1.dequeue())
print(q1.front())
print(q1.getSize())