import time
import threading
from collections import deque
import random as rd

exitflag = 0

class threadlightly(threading.Thread):
   
    def __init__(self, threadID, name,deque):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
        self.d = deque

    def run(self):
        print("starting " + self.name)
        while exitflag == 0:
            shiftn(self.d, 1)
        if exitflag == 1:
            self.exit()

        print("stopping " + self.name)


class printlightly(threading.Thread):

    def __init__(self,threadID,name,deque):

        threading.Thread.__init__(self)
        self.name = name
        self.threadID = threadID
        self.d = deque

    def run(self):
        print("starting " + self.name)
        while exitflag == 0:
            print(self.d)
            print("\n")
       
        if exitflag == 1:

            self.exit()




def shiftn(deque, n):
    
    for i in range(n):
        deque.append(rd.randint(0,10))
        deque.popleft()





d = deque([1,2,3,4,5,7])


thread1 = threadlightly(1,"poppin1",d)
thread2 = printlightly(2,"printin1",d)

thread1.start()
thread2.start()




