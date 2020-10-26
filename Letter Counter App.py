import math
# Basic Data Types Challenge 1: Letter Counter app

print("Welcome in our first program")
var1 = input("Here, let's type your name....")
var2 = var1.title()
print("Hello "+ var2)
print("I will count the number of times that a specific letter occurs in a message.")
var3 = input("Enter a massage.... ")
var4 = input("Which letter would you like to count the occurrences of: ")
var3 = var3.lower()
var4 = var4.lower()

var5 = var3.count(var4)
print(var5)
