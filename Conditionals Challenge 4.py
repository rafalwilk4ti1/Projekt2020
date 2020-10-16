import math
import cmath
import datetime
from math import sqrt
import random
#Conditionals Challenge 16: Shipping Accounts Program

users = ['eramom' , 'footea', 'davisv', 'papinukt', 'allen']
print("Welcome to the Shipping Accounts Program")

user = input("Hello, what is your username: ").lower()

if user in users:
    print("\nHello " +str(user) + ". Welcome back to your account. ")
    print("Current shipping prices are as follows: ")
    ship1 = 5.10
    ship2 = 5.00
    ship3 = 4.95
    ship4 = 4.80
    print("\nShipping orders 0 to 100: " + "\t\t$" + str(ship1) + "0 each")
    print("Shipping orders 100 to 500:" + "\t\t$" + str(ship2) + "0 each")
    print("Shipping orders 500 to 1000:" + "\t$" + str(ship3) + " each")
    print("Shipping orders over 1000: " + "\t\t$" + str(ship4) + "0 each")
    round(ship1,2)
    num_items = int(input("\nHow many items would you like to ship: "))
    if num_items < 100:
        result1 = num_items*ship1
        result1 = round(result1,2)
        print("To ship: " +str(num_items)+ " items will cost you "+str(result1)+"$ at "+str(ship1)+"$ per item.")
    elif num_items >100 and num_items <500:
        result2 = num_items * ship2
        result2 = round(result2, 2)
        print("To ship: " + str(num_items) + " items will cost you " + str(result2) + "$ at " + str(
            ship2) + "$ per item.")
    elif num_items > 500 and num_items <1000:
        result3 = num_items * ship3
        result3 = round(result3, 2)
        print("To ship: " + str(num_items) + " items will cost you " + str(result3) + "$ at " + str(
            ship3) + "$ per item.")
    elif num_items>1000:
        result4 = num_items * ship3
        result4 = round(result4, 2)
        print("To ship: " + str(num_items) + " items will cost you " + str(result4) + "$ at " + str(
            ship4) + "$ per item.")
    answer = input("Would you like to place this order (y/n): ")
    if answer == "y":
        print("Okay. Shipping your "+str(num_items)+" items")
    elif answer == "n":
        print("Okay, no order is being placed at this time.")

else:
    print("You are not on the list, I am sorry, but I have to say goodbye")



#Conditionals Challenge 17: Coin Toss App

print("Welcome in Coint Toss App")
print("\nI will flip a coin a set number of times")
num_flip = int(input("Hey, how many time would you like to toss a coin, bro: "))
yes_no = input("Next question is, would you like to see result of each individual coin flip (yes/no): ").lower()
print("\nFLIPPING!!!")
heads = 0
tails = 0
if yes_no.startswith("y"):
    for x in range(0,num_flip):
        coin = int(random.randint(0, 1))
        if coin == 0:
            heads = heads+1
            print("HEADS")
        elif coin == 1:
            tails = tails+1
            print("TAILS")

        if tails == heads:
            print("At "+str(x+1)+" flips, the number of heads and tails were equal at " +str(heads)+" each.")
    print("\nResults Of Flipping A Coing " +str(num_flip)+" Times: ")
    result_heads = ((heads/num_flip)*100)
    result_heads = round(result_heads,2)
    result_tails = ((tails/num_flip)*100)
    result_tails = round(result_tails,2)
    print("\n Side "+"\t\tCount"+"\t\tPercentage")
    print("Heads "+"\t\t"+str(heads)+"/"+str(num_flip)+"\t\t"+str(result_heads)+"%")
    print("Tails "+"\t\t"+str(tails)+"/"+str(num_flip)+"\t\t"+str(result_tails)+"%")
elif yes_no.startswith("n"):
    for x in range(0,num_flip):
        coin = int(random.randint(0, 1))
        if coin == 0:
            heads = heads+1
        elif coin == 1:
            tails = tails+1

        if tails == heads:
            print("At "+str(x+1)+" flips, the number of heads and tails were equal at " +str(heads)+" each.")
    print("\nResults Of Flipping A Coing " +str(num_flip)+" Times: ")
    result_heads = ((heads/num_flip)*100)
    result_heads = round(result_heads,2)
    result_tails = ((tails/num_flip)*100)
    result_tails = round(result_tails,2)
    print("\n Side "+"\t\tCount"+"\t\tPercentage")
    print("Heads "+"\t\t"+str(heads)+"/"+str(num_flip)+"\t\t"+str(result_heads)+"%")
    print("Tails "+"\t\t"+str(tails)+"/"+str(num_flip)+"\t\t"+str(result_tails)+"%")



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



# Conditionals Challenge 20: Rock, Paper, Scissors App

print("Welcome to a game of Rock, Paper, Scissors")

rounds = int(input("\nHow many rounds would you like to play: "))

moves = ["rock", "paper", "scissors"]
players_score = 0
computer_score = 0


for x in range(1, rounds+1):
    num = random.randrange(0,3)
    print("\nRound: "+str(x))
    print("Player: "+str(players_score)+ "\tComputer: "+str(computer_score))
    move_player = input("Time to pick...rock,paper,scissors: ").lower()
    print("Player: "+str(move_player))
    print("Computer: "+str(moves[num]))
    if move_player == moves[0] and moves[num] == moves[1]:
        print("Computer win!")
        print("Paper covers rock!")
        computer_score += 1
    elif move_player == moves[1] and moves[num] == moves[2]:
        print("Computer win!")
        print("Scissors cut paper!")
        computer_score += 1
    elif move_player == moves[2] and moves[num] == moves[0]:
        print("Computer win!")
        print("")
        computer_score +=1
    elif move_player == moves[1] and moves[num] == moves[0]:
        print("You win!")
        players_score +=1
    elif move_player == moves[2] and moves[num] == moves[1]:
        print("You win!")
        players_score +=1
    elif move_player == moves[0] and moves[num] == moves[0]:
        print("It is a draft! How boring...")
    elif move_player == moves[1] and moves[num] == moves[1]:
        print("It is a draft! How boring...")
    elif move_player == moves[2] and moves[num] == moves[2]:
        print("It is a draft! How boring...")
    elif move_player != moves[0] and move_player != moves[1] and move_player != moves[2]:
        print("I guess, you've type something wrong, that's why computer get a point!")
        computer_score +=1
print("\nFinal Game Results")
print("\tRounds Played: "+str(rounds))
print("\tPlayer Score: "+str(players_score))
print("\tComputer Score:  "+str(computer_score))
if computer_score > players_score:
    print("\tWinner: Computer ")
elif computer_score < players_score:
    print("\tWinner is you!")
else:
    print("The game was a tie... ")
#