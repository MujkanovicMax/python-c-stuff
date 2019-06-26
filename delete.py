import threading
import time
       

class down(threading.Thread):
    
    def __init__(self, threadID, name,rate,size,samp):

        #du rufst den thread als subclass von Th        read auf

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        
        self.rate = rate
        self.size = size
        self.samp = samp

        self.curr = 0.
        

    def run(self):

        #die run methode gibt an was der thread         machen soll während er läuft

        while self.curr < self.size:

            self.curr = self.curr + self.rate/self.samp   

            if self.curr > self.size:

                self.curr = self.size
           
            time.sleep(self.samp)

class dlbar(threading.Thread):

    def __init__(self, threadID, name,dl):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

        self.dl = dl

        self.curr = dl.curr
    def run(self):
       
        print("\033[?25l") #ec kill cursor mark
        print("\033[2J")
        print("\033[;0H"+"_"*48)
        print("\033[2;0H|"+"\033[2;48H|")
        print("\033[3;0H"+"\u203e"*48)

        print("\n");
        print("\n")

        perc = 0
        while perc < 100:

            self.curr = dl.curr
            perc = round(dl.curr/dl.size *100)
 
            var = perc*46/100
            i = round(var)

            if perc > 100:
                perc =100

            for j in range(i):
                print("\033[2;"+str(j+2)+"H#")
                print("\033[4;0H"+str(perc)+"% complete")          

            time.sleep(0.01)
        
        print("\033[4;0HCongratulations, you deleted the Internet")
        self.stopp()

    def stopp(self):


        print("\033[?25h") #ec restore cursor ma                            rk

        print("\n")

#variablengewirr

size = 10000
rate = 0.003
samp = 0.001

#threads werden mit ner id nem namen und den restlichen benötigten variablen aufgerufen

dl = down(1, "dl",rate,size,samp)
dlbarr = dlbar(2,"616", dl)


#die start() methode is in jeder thread klasse automatisch enhalten und führt eigentlich nur dierun() methode aus

dl.start()
dlbarr.start()





