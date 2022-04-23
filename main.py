import threading
import time
import sys

class SecondCounter(threading.Thread):
    '''
    create a thread object that will do the counting in the background
    default interval is 1/1 of a second
    '''
    def __init__(self, interval=1):
        # init the thread
        threading.Thread.__init__(self)
        self.interval = interval  # seconds
        # initial value
        self.value = 0
        # controls the while loop in method run
        self.alive = False

    def run(self):
        '''
        this will run in its own thread via self.start()
        '''
        self.alive = True
        while self.alive:
            time.sleep(self.interval)
            # update count value
            self.value += self.interval

    def peek(self):
        '''
        return the current value
        '''
        return self.value

    def finish(self):
        '''
        close the thread, return final value
        '''
        # stop the while loop in method run
        self.alive = False
        return self.value


def intro():
  while True:
       print("╔════════════════════════════════════════╗")
       print("")
       n = input("  Please enter your first name ➣ ")
       if n.isalpha():
           print("    ----------------------")
           print("    Hello! " +      n)
           print("    ----------------------")
           print("")
           break
       else:
           print("  Please enter your first name with letters only, and don't leave empty spaces")
           
  
  
  inst=input("  Press enter to proceed  :")
  print("")
  print("╚════════════════════════════════════════╝")
  if inst=="y":
      print("")
      print("")
  else:
      print("")
      print("")
      print("╭⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╮")
      print("     ▏WELCOME TO MY MATH QUIZ FELLOW COMPUTER SCIENCE MEMBERS! ▏")
      print("╰⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╯")
def information():