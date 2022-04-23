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
  # QUESTION 3
  answer3 = input(
      "What is 4 * 245.6 ? \n a. 345.8 \n b. 982.4 \n c. 456.6 \nAnswer: ")
  if answer3 == "b" or answer3 == "982.4":
      score += 1
      print("Correct!")
      print("Score: ", score)
      print("\n")
  else:
      print("Incorrect! The right answer is 982.4")
      print("Score:", score)
      print("\n")
    #FINAL MESSAGE
  if score <= 1:
      print("You total score:", score, "- You did Okay!")
  elif score == 2:
      print("You total score:", score, "- You did Good!")
  elif score == 3:
      print("You total score:", score, "- You did Amazing!")
  print("╚════════════════════════════════════════════════════════════════════════════════╝")
  print("")
  print("")
  print("╔════════════════════════════════════════════════════════════════════════════════╗")
  print("")
def scoring_system():
  print("--) \033[4m-Now that is over we can move on to the actual quiz\033[0m")
  #How many points each question is worth;
  print("Scoring System:")
  
  print("Achieved Questions:+ 1 POINT")
  print("Merit Questions:+ 2 POINTS")
  print("Excellence Questions:+ 3 POINTS")
  print("")
def timer():
  # make this work with Python2 or Python3
  #if sys.version_info[0] < 3:
     # input = raw_input
  global count
  # create the class instance
  count = SecondCounter()
  # start the count
  count.start()
  
  # test the counter with a key board response time
  # or put your own code you want to background-time in here
  # you can always peek at the current counter value
  e = input("Press Enter for timer to start")

#start of program
def questions():
  questions={'\033[4mQuestion 1\033[0m.\nMosie is starting her own badminton court hire company.She will charge $10 per hour,along with a fixed charge of $8,Find the Equation of Mosies court fees, when x is = hours\n❒ a: 15x+8\n❒ b: 8x+15x\n❒ c: 10x+8 \n' : 'c' , 
        '\033[4mQuestion 2\033[0m\nA building inspector wants to check if the pillar of the building is perpendicular to the ground. He measures the distance between 3 points, Each distance measures 3.11m, 4.19m and 5.23m. Is the pillar of the building of the building perpendicular to the ground.\n❒ a: Yes\n❒ b: No\n❒ c: Impossible to tell \n' : 'a' ,
        '\033[4mQuestion 3\033[0m\nWanipun takes 35 minutes to jog the 10 km from his home to school. What  is the average speed when she is jogging from his home to school?\n❒ a: 1.15km/min\n❒ b: 0.125km/ min\n❒ c: 17.15km/min\n' : 'b' ,
        '\033[4mQuestion 4\033[0m\nWhat is the value of 2x^4 − 3x + 5 when x = − 2?\n❒ a: 46\n❒ b: 25\n❒ c: 43 \n' : 'c'}
   
  for key in questions.keys():
            global score
            user_answer=input(key)
            if questions.get(key)==user_answer:
                score +=1
                print("")
                print("╭⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╮")
                print("Good Job, That's Correct!  ✅")
                print("╰⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╯")
                print("")
                print("╚════════════════════════════════════════════════════════════════════════════════╝")
                print("")
                print("╔════════════════════════════════════════════════════════════════════════════════╗")
                print("")
            else:
                print("")
                print("╭⎯⎯⎯⎯⎯⎯⎯╮")
                print("Incorrect  ❎")
                print("╰⎯⎯⎯⎯⎯⎯⎯╯")
                print("╚════════════════════════════════════════════════════════════════════════════════╝")
                print("")
                print("╔════════════════════════════════════════════════════════════════════════════════╗")
        
        
        
  questions={'\033[4mQuestion 5\033[0m.\nFollwing on from question 2\nFrom 8m away from the bottom of the left side of the building he looks at the top of the bridge. The angle of elevation is 28 degrees. He is 1.83m  tall. Find the height of the building.\n❒ a: 6.08m(2.d.p)\n❒ b: 6.56m(2.d.p)\n❒ c: 8.40m(2.d.p) \n' : 'a' ,
        '\033[4mQuestion 6\033[0m\nFind the co-ordinates of which the follwing two lines intersect at.4x+10, 2x+18\n❒ a:(2,18)\n❒ b:(-4,26)\n❒ c:(4,26) \n' : 'c'
        , '\033[4mQuestion \033[0m7\nGiven the equation -x/2(x-r)+2 find the equation of r given the point(8,2)\n❒ a: 6\n❒ b: 8\n❒ c: 10\n' :  'b' 
        ,  '\033[4mQuestion 8\033[0m\n75% of homes on the national power supply in New Zealand are in the North Island. The rest are in the South Island. 70% of homes in the North Islandand 80% of homes in the South Island use electricity for their heating.   Calculate the probability that a home selected randomly across New Zealandis on the national power supply in the North Island AND uses electricity  for heating.\n❒ a: 0.5(1/2)\n❒ b: 0.525(21/40)\n❒ c: 0.593(16/27) \n' : 'b'}
        
  for key in questions.keys():
            user_answer=input(key)
            if questions.get(key)==user_answer:
                score += 2 
                print("")
                print("╭⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╮")
                print("Good Job, That's Correct!  ✅")
                print("╰⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╯")
                print("")
                print("╚════════════════════════════════════════════════════════════════════════════════╝")
                print("")
                print("╔════════════════════════════════════════════════════════════════════════════════╗")
                print("")
            else:
                print("")
                print("╭⎯⎯⎯⎯⎯⎯⎯╮")
                print("Incorrect  ❎")
                print("╰⎯⎯⎯⎯⎯⎯⎯╯")
                print("╚════════════════════════════════════════════════════════════════════════════════╝")
                print("")
                print("╔════════════════════════════════════════════════════════════════════════════════╗")
        
  questions={'\033[4mQuestion 9\033[0m\nLulu and Pika are standing on opposites sides of the net Pika sends the ball over the net towards Lulu. The equation of the path travelled by the ball is H=-0.25(x-2.1)^2+3.9.Find when the ball will hit the ground.\n❒ a: 6m away from the net\n❒ b: 6.05m away from the net\n❒ c: 12.24m  away from the net \n': 'b'
        ,'\033[4mQuestion 10\033[0m\nFollowing on from Question 8\nThere are 1 500 000 homes across New Zealand (both in the North Island and the South Island). Calculate how many of the homes on the national power supply in the South Island do not use electricity for heating. \n❒ a: 75,000\n❒ b: 125,000\n❒ c: 265,000 \n' : 'a'
         
        ,'\033[4mQuestion 11\033[0m\n3/x+2+5/x-4=2\n❒ a: 7,-1\n❒ b: 3,6\n❒ c: 7\n': 'a'
        , '\033[4mQuestion 12\033[0m\n36x6^2x+6=6^x^2\n❒ a: x=4\n❒ b: x=3,1\n❒ c: x=4,-2\n':  'c'}
        
  for key in questions.keys(): 
            user_answer=input(key)
            if questions.get(key)==user_answer:
                score += 3
                print("")
                print("╭⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╮")
                print("Good Job, That's Correct!  ✅")
                print("╰⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯╯")
                print("")
                print("╚════════════════════════════════════════════════════════════════════════════════╝")
                print("")
                print("╔════════════════════════════════════════════════════════════════════════════════╗")
                print("")
            else:
                print("")
                print("╭⎯⎯⎯⎯⎯⎯⎯╮")
                print("Incorrect  ❎")
                print("╰⎯⎯⎯⎯⎯⎯⎯╯")
                print("╚════════════════════════════════════════════════════════════════════════════════╝")
                print("")
                print("╔════════════════════════════════════════════════════════════════════════════════╗")
                
  print("")



