import threading
import numpy as np


class sine(threading.Thread):

    def __init__(self,angle):
        super(sine,self).__init__()

        self.a = angle
        self.s = 0

    def run(self):

        self.s = np.sin(self.a)
        


class cosine(threading.Thread):

    def __init__(self,angle):
        super(cosine,self).__init__()
        self.a = angle
        self.s = 0

    def run(self):

        self.s = np.cos(self.a)


t1 = sine(2/3.*np.pi)
t2 = cosine(1/3. * np.pi)
t1.start()
t2.start()
t1.join()
t2.join()

print(t1.s + t2.s, np.sin(2/3.*np.pi)+np.cos(1/3.*np.pi))


