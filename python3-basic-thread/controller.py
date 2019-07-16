#! /usr/bin/env python3
from mythread import MyThread

for i in range(10):
    print("i = ", i)
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()
