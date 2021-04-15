import math
import cmath
import datetime
from math import sqrt
import random


#Conditionals Challenge 18: Voter Registration App

print("Welcome to the Voter Registration App")

name = input("What's your name bro: ").capitalize()
age = int(input("How old are you mate: "))

parties = ["Republican", "Democratic", "Independent", "Libertarian", "Green"]


if age > 18:
    print("\nCongratulations "+str(name)+"! You are old enough to register to vote")
else:
    print("\nNot this time, baby... ;)")

print("Here is a list of political to join: ")
for x in parties:
    print("-"+str(x))

joining = input("\nWhat party would you like to join: ").capitalize()

print("Congratulations "+str(name)+"! You have joined the "+str(joining)+" party")
print("This is major party!")
