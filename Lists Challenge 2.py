import math
import cmath
import datetime
from math import sqrt
import random
# Lists Challenge 6 - Grade Sorter App

print("Welcome to the Grade Sorter App")
grades = []
grade1 = int(input("\nWhat is your first grade (0-100): "))
grade2 = int(input("What is your first grade (0-100): "))
grade3 = int(input("What is your first grade (0-100): "))
grade4 = int(input("What is your first grade (0-100): "))
grades.append(grade1)
grades.append(grade2)
grades.append(grade3)
grades.append(grade4)
print("\nYour grades are: " + str(grades) + ".")
grades.sort(reverse=True)
print("\nYour grades from highest to lowest are: " + str(grades)+".")

print("\nThe lowest two grades will now be dropped.")
remove_grade = grades.pop()
print("Removed grade: "+ str(remove_grade) +".")
remove_grade = grades.pop()
print("Removed grade: "+ str(remove_grade) +".")
print("\nYour remaining grades are: "+str(grades)+".")
print("\nNice work! Your highest grade is a "+str(grades[0]))
# Lists Challenge 7  - Different Types of Lists Program

# Making 4 lists
num_strings = ["15","100","55","42"]
num_ints = [15,100,55,42]
num_floats = [1.2, 2.3, 3.4, 4.5]
num_lists = [[1,2,3,],[4,5,6],[7,8,9]]

# First 3 sentenceses
num_strings = type(num_strings)
print("\t\t\t Summary Table")
print("\nThe variable num_strings is a " +str(num_strings) +".")
num_strings = ["15","100","55","42"]
print("It contains the elements: ", num_strings ,".")
num1 = type(num_strings[0])
print("The element", num_strings[0], "is a ", num1 , "." )

# Second 3 sentences
num_ints = type(num_ints)
print("\nThe variable num_ints is a ",str(num_ints) ,".")
num_ints = [15,100,55,42]
print("It contains the elements: ",num_ints,".")
num2 = type(num_ints[0])
print("The element",num_ints[0],"is a",num2,".")

# Third 3 sentences
num_floats = type(num_floats)
print("\nThe variable num_floats is a", str(num_lists),".")
num_floats = [0.2, 2.3, 3.4, 4.5]
print("It contains the elements: ",num_floats ,".")
num3 = type(num_floats[0])
print("The element",num_floats[0],"is a ",num3,".")


# Fourth 3 sentences
num_lists = type(num_lists)
print("\nThe variable num_lists is a ",str(num_lists),".")
num_lists = [[0,2,3,],[4,5,6],[7,8,9]]
print("It contains the elements: ",num_lists,".")
num4 = type(num_lists[0])
print("The element", num_lists[0], "is a ",num4,".")


num_strings = ["15","100","55","42"]
num_ints = [15,100,55,42]
num_floats = [1.2, 2.3, 3.4, 4.5]
num_lists = [[1,2,3,],[4,5,6],[7,8,9]]

num_strings.sort()
num_ints.sort()
print("\nNow sorting num_strings and num_ints...")
print("Sorted num_strings: ", num_strings,".")
print("Sorted num_ints: ",num_ints, ".")

print("\nStrings are sorted alphabetically while integers are sorted numerically!")


# Lists Challenge 8: Grocery List App

your_list = ["Meat", "Cheese"]

print("Welcome to the Grocery List App")
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

print("Current Date and Time:",month,"/",day,hour,":",minute,".")
print("You currently have ",your_list[0]," and ",your_list[1], "in your list.")

your_list.append(str.title((input("\nType of food to add to the grocery list: "))))
your_list.append(str.title((input("Type of food to add to the grocery list: "))))
your_list.append(str.title((input("Type of food to add to the grocery list: "))))
print("\nHere is your grocery list: ")
print(your_list)
print("Here is your grocery list sorted: ")
your_list.sort()
print(your_list)
print("\nSimulating grocery shopping...")

print("\n Current grocery list: ",len(your_list),".")
print(your_list)
rem = str.title(input("What food did you just buy: "))
your_list.remove(rem)
print("Removing" ,str(rem), "from list...")
print(your_list)

print("\n Current grocery list: ",len(your_list),".")
print(your_list)
rem = str.title(input("What food did you just buy: "))
your_list.remove(rem)
print("Removing" ,str(rem), "from list...")
print(your_list)

print("\n Current grocery list: ",len(your_list),".")
print(your_list)
rem = str.title(input("What food did you just buy: "))
your_list.remove(rem)
print("Removing" ,str(rem), "from list...")

print("Current grocery list: ",len(your_list),"items")
print(your_list)

old_product = your_list[-1]
print("\n Sorry, the store is out of",old_product, ".")
new_product = input("What would you like instead: ")
your_list.remove(old_product),your_list.append(str.title(new_product))
print("\nHere is what remains on your grocery list:")
print(your_list)

# Lists Challenge 9: Basketball Roster Program
print("Welcome to the Basketball Roaster Program")
roster = []
point_guard = str.title(input("\nWho is you point guard: "))
roster.append(point_guard)
shooting_guard = str.title(input("Who is your shooting guard:  "))
roster.append(shooting_guard)
small_forward = str.title(input("Who is your power forward: "))
roster.append(small_forward)
power_forward = str.title(input("Who is your power forward: "))
roster.append(power_forward)
center = str.title(input("Who is your center: "))
roster.append(center)

print("\n\tYour starting 5 for the upcoming basketballl season")
print("\tPoint Guard: ","\t\t\t\t",roster[0])
print("\tShooting Guard: ","\t\t\t",roster[1])
print("\tSmall Forward: ","\t\t\t",roster[2])
print("\tPower Forward: ","\t\t\t",roster[3])
print("\tCenter: ","\t\t\t\t\t",roster[4])
injured_player = roster[2]
print("\nOh no,",roster[2],"is injured.")
roster.remove(roster[2])
print("Your roster only has ",len(roster),"players")
added_player = input("Who will take "+ injured_player +"'s spot: ").title()
roster.insert(2, added_player)

print("\n\tYour starting 5 for the upcoming basketballl season")
print("\tPoint Guard: ","\t\t\t\t",roster[0])
print("\tShooting Guard: ","\t\t\t",roster[1])
print("\tSmall Forward: ","\t\t\t",roster[2])
print("\tPower Forward: ","\t\t\t",roster[3])
print("\tCenter: ","\t\t\t\t\t",roster[4])

print("\nGood luck", roster[2], "you will do great!")
print("Your roster now has", len(roster), "players")



# Lists challenge 10: Favourite Teachers Program
print("Welcome to the Favorite Teachers Program")
fav_techears = []
fav_techears.append(input("\nWho is your first favorite teacher: ").title())
fav_techears.append(input("Who is your second favorite teacher: ").title())
fav_techears.append(input("Who is your third favorite teacher: ").title())
fav_techears.append(input("Who is your fourth favorite teacher: ").title())
print("\nYour favourite teachers are: " + str(fav_techears)+".")
print("Your favourite teachers alphabetically order are: "+ str(sorted(fav_techears)))
print("Your favourite teachers in reverse alphabetical order are: " +str(sorted(fav_techears, reverse=True)))
print("\nYour top two techears are: "+fav_techears[0]+" and "+fav_techears[1])
print("your next two teacher two favourite teachers are: "+fav_techears[2]+" and "+fav_techears[3]+".")
print("Your last favourite teacher is: " + fav_techears[-1])
print("You have a total of" ,len(fav_techears), "favourite teachers")

print("\nOops, ",fav_techears[0], "is no longer your first teacher. Who is your new FAVOURITE teacher:")
new_fav = str.title(input())
fav_techears.insert(0,new_fav)
print("\n","Your favourite teachers ranked are: ",fav_techears)
print("Your favourite teachers alphabetically are: " + str(sorted(fav_techears)))
print("Your favourite teachers in reverse aplhabetical order are: " + str(sorted(fav_techears, reverse=True)))

print("\nYour top two teachers are: "+fav_techears[0] + " and " + fav_techears[1])
print("Your next two favourite teachers are: "+ fav_techears[2] +" and "+fav_techears[3])
print("Your last favourite teacher is: "+ fav_techears[-1])
print("You have a total of "+ str(len(fav_techears))+" favourite teachers.")

fav_techears.remove(input("\nYou've decided you no longer like a teacher. Wich teacher would you like to remove from you list: ").title())

print("\nYour favourite teachers ranked are: " + str(fav_techears))
print("Your favourite teachers ranked are: " + str(sorted(fav_techears)))
print("Your favourite teachers ranked are: " + str(sorted(fav_techears, reverse=True)))


print("\nYour top two teachers are: "+fav_techears[0]+" and "+fav_techears[1])
print("Your next two favourite teachers are : "+fav_techears[2]+" and "+fav_techears[3])
print("Your last favourite teacher is: "+fav_techears[-1])
print("You have a total of "+str(len(fav_techears))+" favourite teachers")
