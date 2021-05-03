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
#
# Basic Data types Challenge 2: Miles Per Hour Conversion App
print("Hello, this is The MIles Per Hour Conversion App")
speed_mls = float(input("Your speed in miles per hour: "))
speed_mps = speed_mls*0.4474
speed_mps = round(speed_mps,2)
print("Your speed in meters per second is " + str(speed_mps) + ".")
# Basic Data Types Challenge 3: Temperature Conversion App


print("Welcome to the Temperature Conversion App")
f = float(input("Give me temperature in Fahrenheit: "))

c = (f-32) * 5/9
c = round(c,4)

k = (f-32)/1.8000 + 273.15
k = round(k,4)
print("Degrees Fahrenheit: "+"\t"+ str(f) + ".")
print("Degrees Celsius: "+ "\t"+"\t"+ str(c) + ".")
print("Degrees Kelvin: "+ "\t"+"\t"+str(k) + ".")




# Basic Data Types Challenge 4 - Right Triangle Solver App
print("Welcome to the Right Triangle Sover App")
leg1 = float(input("What is the first leg of the triangle: "))
leg2 = float(input("What is the second leg of the triangle: "))

leg3 = math.sqrt(leg1**2 + leg2**2)
leg3 = round(leg3,3)

area = 0.5 * leg1 * leg2
area = round(area, 3)

print("For a triangle with " + str(leg1)+ " and " + str(leg2)+" the hypotenus is " +str(leg3) + "."  )
print("For a triangle with " + str(leg1)+ " and " + str(leg2)+" the area is " +str(area) + "."  )
#
# Basic Data Types Challenge 5  - Multiplication/Exponent Table App

print("Welcome to the Multiplication/Exponent Table App")
name = input("Give me your name: ")
number = float(input("Give me your number: "))
message = name.title()+ " Math is cool!"
Multiplication Table
print("\nMultiplication Table for: " + str(number))

print("\t"+"1.0 * "+str(number)+" = " + str(round(1*number,4)))
print("\t"+"2.0 * "+str(number)+" = " + str(round(2*number,4)))
print("\t"+"3.0 * "+str(number)+" = " + str(round(3*number,4)))
print("\t"+"4.0 * "+str(number)+" = " + str(round(4*number,4)))
print("\t"+"5.0 * "+str(number)+" = " + str(round(5*number,4)))
print("\t"+"6.0 * "+str(number)+" = " + str(round(6*number,4)))
print("\t"+"7.0 * "+str(number)+" = " + str(round(7*number,4)))
print("\t"+"8.0 * "+str(number)+" = " + str(round(8*number,4)))
print("\t"+"9.0 * "+str(number)+" = " + str(round(9*number,4)))

#
print("\nExponent Table for "+ str(number))
Exponent
print("\t"+str(number) + " ** 1 = "+ str(round(number**1,4)))
print("\t"+str(number) + " ** 2 = "+ str(round(number**2,4)))
print("\t"+str(number) + " ** 3 = "+ str(round(number**3,4)))
print("\t"+str(number) + " ** 4 = "+ str(round(number**4,4)))
print("\t"+str(number) + " ** 5 = "+ str(round(number**5,4)))
print("\t"+str(number) + " ** 6 = "+ str(round(number**6,4)))
print("\t"+str(number) + " ** 7 = "+ str(round(number**7,4)))
print("\t"+str(number) + " ** 8 = "+ str(round(number**8,4)))
print("\t"+str(number) + " ** 9 = "+ str(round(number**9,4)))

print("\n" + message)
print("\t" + message.lower())
print("\t\t" + message.title())
print("\t\t\t" + message.upper())