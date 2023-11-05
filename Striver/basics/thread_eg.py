from ast import arg
from re import T
from threading import Thread
import time

def eat():
    time.sleep(3)
    print("Ate breakfast")

def drink():
    time.sleep(4)
    print("Drank coffee")

def study():
    time.sleep(5)
    print("Done homework")

x = Thread(target=eat, args=())
x.start()

y = Thread(target=drink, args=())
y.start()

z = Thread(target=study,args=())
z.start()

# eat()
# drink()
# study()