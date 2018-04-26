'''
Created on Apr 26, 2018

@author: ankusain
'''
import random
hc = random.randrange(1,101)
winner = False
Counter = 0
while not winner: 
    Counter += 1
    userInput = input("Enter a number: ")
    userNum = int(userInput)
    
    if hc > userNum:
        print("Your guess is too low!")
    elif hc < userNum:
        print("Your guess is too high!")
    else:
        print("You win!!")
        print("in " + str(Counter) + " tries")
        winner = True


    