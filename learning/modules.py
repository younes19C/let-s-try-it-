#model = a file containing python code .may contain fonctions, classes,ets.
# use with modular programming , wich is to separate a program into parts 
import messages as msg
#importing the messages module 
#from messages import hello,bye
#from messages import *
msg.hello()
msg.bye()
# help("modules")
#help("datetime")

import random 
choice=["rock","scisser","paper"]
computer=random.choice(choice)

player=input("rock,scisser,paper")
print("your choice is :",player)
print("computer choice is :",computer)
