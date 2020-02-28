from threading import *
from time import sleep

def hello():
    i = 1
    while i<=5:
        print("Hello")
        sleep(1)
        i +=1

def hi():
    i = 1
    while i<=5:
        print("Hi")
        sleep(1)
        i += 1

t1 = Thread(target=hello)
t2 = Thread(target=hi)
t1.start()
t2.start()


t1.join()
t2.join()

print("Bye")


class Hello(Thread):
    def run(self):
        i = 1
        while i <= 5:
            print("Class: Hello")
            sleep(1)
            i += 1

class Hi(Thread):
    def run(self):
        i = 1
        while i <= 5:
            print("Class: Hi")
            sleep(1)
            i += 1

t1 = Hello()
t2 = Hi()
t1.start()
t2.start()
