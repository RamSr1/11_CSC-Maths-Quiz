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
#The Instructions/Knowledge for the user to keep in mind;
  print("")
  print("\033[4mHow This Quiz Will Work:\033[0m")
  print("")
  print("╔═══════════════════════════════════════════════════════════════════════════════╗")
  print("")
  print("1) \033[4mThis Quiz Will Have A Total Of 12 Question For You To Answer.\033[0m")
  print("")
  print("2) \033[4mYou Will Have 1 Chance To Answer Each Question Correctly.\033[0m")
  print("")
  print("3) \033[4mEvery Question Will Include A Range Of Different Math Skills.\033[0m")
  print("")
  print("4) \033[4mEach Question Has It's Own Difficulty And Are Randomised.\033[0m")
  print("")
  print("5) \033[4mQuestions Will Consist Of Achieved, Merit Or Excellence Difficulty.\033[0m")
  print("")
  print("6) \033[4mAnswer Carefully As Every Question Counts Towards Your Final Score.\033[0m")
  print("")
  print("7) \033[4mThis Quiz Is To Prepare and Test Your NCEA Level 1 Maths Skills.\033[0m")
  print("")
  print("8) \033[4mNote: If characters/spaces are inputted the quiz will not prompt and ask again!.\033[0m")
  print("")
  print("╚════════════════════════════════════════════════════════════════════════════════╝")
  print("") 
  print("")
  print("╔════════════════════════════════════════════════════════════════════════════════╗")
  print("")
def warmup():
  print("\033[4m Here is a 3 question warmup, this won't affect your grade it is just a starter.\033[0m")
  global score
  score = 0
  
  # QUESTION 1
  answer1 = input("What is 2 * 20 ? \n a. 35 \n b. 40 \n c. 28 \nAnswer: ")
  if answer1 == "b" or answer1 == "40":
      score += 1
      print("Correct!")
      print("Score: ", score)
      print("\n")
  else:
      print("Incorrect! The right answer is 40")
      print("Score: ", score)
      print("\n")
  # QUESTION 2
  answer2 = input("What is 5 * 50 ? \n a. 350 \n b. 400 \n c. 250 \nAnswer: ")
  if answer2 == "c" or answer2 == "250":
      score += 1
      print("Correct!")
      print("Score: ", score)
      print("\n")
  else:
      print("Incorrect! The right answer is 250")
      print("Score:", score)
      print("\n")