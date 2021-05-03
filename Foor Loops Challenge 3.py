import math
import cmath
import datetime
from math import sqrt
import random

#For Loops Challenge 11: Binary Hexadecimal Converter App
print("Welcome to the Binary/Hexadecimal Converter App")

value = int(input("\nCompute binary and hexadecimal values up to the following decimal number: "))
print("Gererating lists... complete!")
decimal_values = list(range(1, value))
binary_values = []
hexadecimal_values = []
for i,y in zip(decimal_values,decimal_values):
    binary_values.append(bin(i))
    hexadecimal_values.append(hex(y))
print("\nUsing slices, we will now show you a portion of each list.")
dec_num1 = int(input("What decimal number would you like to start at: "))
dec_num2 = int(input("What decimal number would you like to stop at: "))


print("\nDecimal values from " + str(dec_num1) + " to " + str(dec_num2)+":")
for x in decimal_values[(dec_num1-1):dec_num2]:
    print(x)

print("\nBinary values from "+str(dec_num1) +" to " +str(dec_num2)+": ")
for x in binary_values[(dec_num1-1):dec_num2]:
    print(x)

print("\nHexadecimal values from "+str(dec_num1)+" to "+str(dec_num2)+":")
for x in hexadecimal_values[(dec_num1-1):dec_num2]:
    print(x)

input("Press Enter to see all values from 1 to 12")
print("Decimal----Binary----Hexadecimal")
print("---------------------------------")
for a,b,c in zip(decimal_values,binary_values,hexadecimal_values):
    print(str(a)+"----"+str(b)+"----"+str(c))


#For Loops Challenge 12: Quadratic Equation Solver App

print("Welcome to the Quadratic Equation Solver App")

print("\n A quadratic equation is of the form ax^2 + bx + c = 0")
print("Your solutions can be real or complex numbers. ")
print("A complex number has two parts: a + bj")
print("Where a is the real portion and bj is the imaginary portion")
list_of_numbers = []
num_of_equation = int(input("\nHow many equations would you like to solve today: "))
for num_of_equation in range(1, num_of_equation+1):
    list_of_numbers.append(num_of_equation)
for i in list_of_numbers:
    print("\nSolving equation #" +str(list_of_numbers[0]))
    list_of_numbers.remove(list_of_numbers[0])
    print("--------------------------------------")
    a = float(input("Please enter your value of a(coefficient of x^2):" ))
    b = float(input("Please enter your value of b(coefficient of x):" ))
    c = float(input("Please enter your value of a(coefficient):" ))
    print("\nThe sollutions to" ,a, "x^2 + " ,b, "x +" ,c, "=0")
    delta = b**2 - (4*a*c)

    x1 = (-b - delta * (1/2))/(2*a)
    x2 = (-b + delta * (1/2))/(2*a)
    print("\nx1 = (",x1,"+",b,")")
    print("x2 = (",x2,"-",b,")")
print("\nThank you for using the Quadratic Equation Solver App. Goodbye")

# For Loops Challenge 13: Factorial Calculator App

print("Welcome to the Factorial Calculator App")

number = int(input("\nWhat number would you like to compute the factorial of: ?"))
print(str(number) + "! =", end="")
for i in range(0 , number+1):
    print(str(i), end="*")
print(str(number))

x = math.factorial(number)
print("\nHere is the result fronm the math library: ")
print("The factorial of "+str(number)+" is "+str(x)+"!")

fact = 1
for i in range(1 , number+1):
    fact = fact * i

print("\nHere is the result from my own algorithm: ")
print("The factorial of "+str(number)+" is " + str(fact)+"!")

print("\nIt is shown twice that "+str(number)+"! ="+str(fact)+"with excitement")

# For Loops Challenge 14: Fibonacci Calculator App

print("Welcome to the Fibonacci Calculator App")

num = int(input("How many digits of the Fibonacci Sequence would you like to compute: "))
fib = [1,1]
for i in range(num-2):
    new_fib = fib[i] + fib[i+1]
    fib.append(new_fib)
print("The first 15 numbers of the Fibonacci sequence are: ")
for i in fib:
    print(i)

print("The corresponding Godler Ratio values are: ")
new_fib_list = []
for i in range(num-2):
    divide_number = fib[i]/fib[i-1]
    new_fib_list.append(divide_number)

for i in new_fib_list:
    print(i)


print("The ratio of consecutive Fibonacci terms approaches Phi; 1.618....")


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
#