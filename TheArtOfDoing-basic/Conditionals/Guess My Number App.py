import math
import cmath
import datetime
from math import sqrt
import random
# Conditionals Challenge 19: Guess My NUmber App

print("Welcome to the Guess My Number App")

name = input("\nHello! What is your name: ").capitalize()
print("Well "+str(name)+" I am thinking of a number between 1 and 20.")

random_num = random.randrange(1,20)

trying = []
print(random_num)
for x in range(1,6):
    guess = int(input("\nTake a guess: "))
    trying.append(guess)
    result_trying = len(trying)
    if  guess < random_num and result_trying != 5:
        print("Your number is too low")
    elif guess > random_num and result_trying != 5:
        print("Your number is too high")
    else:
        if random_num == guess:
            print("Congratulations "+str(name)+", you win this game , in "+str(result_trying)+" try :)")
        else:
            print("Game Over. You lose brother, this number I was thinking of was "+str(random_num)+".")
