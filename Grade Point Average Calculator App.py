import math
import cmath
import datetime
from math import sqrt
import random

#For Loops Challenge 15: Grade Point Average Calculator App

print("Welcome to the Average Calculator App")

name = input("What is your name: ").title()
grades = int(input("How many grades would you like to enter: "))
grades_list = []
for i in range(0, grades):
    i = int(input("Enter grade: "))
    grades_list.append(i)

grades_list.sort(reverse=True)
print("Grades Highest to Lowest: ")
for i in grades_list:
    print("\t"+str(i))
print("\n"+ str(name)+ "'s Grade Summary: ")
print("\tTotal number of Grades: " + str(len(grades_list)))
print("\tHighest Grade: " + str(grades_list[0]) )
print("\tLowest Grade:" + str(grades_list[-1]))
average = sum(grades_list)/len(grades_list)
average = sum(grades_list)/len(grades_list)
print("\tAverage: " + str(average))
average = float(average)
average = round(average,2 )
suma = sum(grades_list)
desired_average = float(input("\nWhat is your desired average: " ))
new_num = desired_average * float(len(grades_list)+1) - float(sum(grades_list))
new_num = round(new_num,2)
print("\nGood luck " + str(name) + "!")
print("You will need to get a " +str(new_num)+ " on your next assignment to eaern a "+ str(desired_average)+" average.")
print("let's see what your average could have been if you did better/worse on an assignment")
copy_list = grades_list[:]
print(copy_list)
first_num =  int(input("\nWhat grade would you like to change: "))
sec_num = int(input("What grade would you like to change " +str(first_num) +" to: "))
grades_list.remove(first_num)
grades_list.append(sec_num)
grades_list.sort(reverse=True)

print("\nNew Grades Highest to Lowest: ")
for i in grades_list:
    print("\t"+str(i))


print("\n"+str(name)+"'s New Grade Summary:")
print("\tTotal number of Grades: "+str(len(grades_list)))
print("\tHighest Grade: "+str(grades_list[0]))
print("\tLowest Grade: " + str(grades_list[-1]))
average_2 = sum(grades_list)/len(grades_list)
print("\tAverege: "+ str(average_2))
print("\nYour new average would be a: "+str(average_2)+" compared to your real average of "+str(average)+"!")
print("That is a change of "+str(average_2-average)+" points!")

print("Too bad your original grades are still the same!")
print(copy_list)
print("You should go ask for extra credit")



average = suma + nastepnaocena / int(len(grades_list)+1)
nastepna ocena = average*len(grades_list) + 1

print("You will need to get a "+ +"on your next assignment to earn a "++" average. ")