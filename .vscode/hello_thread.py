from multiprocessing import Process
import os

def f(name):
    for i in range(1000):
        print('## %s(%s) : %d ##' % (name, os.getpid(), i))

# multi-process
if(__name__ == '__main__'):
    print("Are you ready?")
    p = Process(target=f, args=('rabbit',))
    p.start()

    for i in range(1000):
        print('** %s(%s) : %d **' % ('wolf', os.getpid(), i))

    p.join()
    print('We finished the task.')


