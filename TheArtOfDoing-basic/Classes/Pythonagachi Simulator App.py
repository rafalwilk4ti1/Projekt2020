import random

class creature():
    """Define a creature in the game"""
    def __init__(self,name):
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food = 2
        self.is_sleeping = False
        self.is_alive = True


    def eat(self):
        """It is using to eating by creature """
        if self.food >0:
            self.food -=1
            number = random.randint(1,4)
            self.hunger -= number
            print("\nOmnomnom it was yummy, grrr. :)")
        else:
            print("\nI regret to inform you, there is no food for you :(")
        if self.hunger < 0:
            self.hunger = 0

    def play(self):
        number = random.randint(0,2)
        print("\n"+str(self.name)+ " wants to play a game")
        print("\n"+str(self.name)+ " thinks of a number 0 , 1 or 2.")
        guess = int(input("\nLet's guess what a number creature may thinks"))
        if guess == number:
            print("\nThe guess is correct!")
            self.boredom -=3
        else:
            print("\nUnfortunately your guess is incorrect")
            self.boredom -=1
        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True
        self.tiredness -=3
        self.boredom -=2
        print("\n"+str(self.name) + "is sleeping")
        if self.tiredness < 0:
            self.tiredness = 0
        elif self.boredom < 0:
            self.boredom = 0



    def awake(self):
        number = random.randint(0,2)
        if number == 0:
            print("\nOur "+str(self.name)+ " has just woke up.:)")
            self.is_sleeping = False
            self.tiredness = 0
        else:
            print("\nOur "+str(self.name)+ " is continue sleeping ;)")
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print("\n"+str(self.name)+ " has took a bath, now it's clean.")


    def forage(self):
        food_found = random.randint(0,4)
        self.food += food_found
        self.dirtiness += 2
        print("\n"+str(self.name)+ "found "+str(self.food)+" pieces of food! :)")

    def show_values(self):
       print("\nCreature name: "+ str(self.name))
       print("Hunger (0-10): "+str(self.hunger))
       print("Boredom(0-10): "+str(self.boredom))
       print("Tiredeness(0-10): " +str(self.tiredness))
       print("Dirtiness(0-10): "+str(self.dirtiness))
       print("\nFood Inventory: "+str(self.food)+" pieces.")
       if  self.is_sleeping:
            print("Current Status: Sleeping")
       else:
           print("Current Status: Awake ")

    def incriment_values(self, difficult):
        number = random.randint(0,difficult)
        self.hunger += number
        if self.is_sleeping == False:
            self.boredom += number
            self.tiredness += number
        self.dirtiness += number


    def kill(self):
        if self.hunger >= 10:
            print("\nYour creature died from starving")
            self.is_alive = False
        elif self.dirtiness >=10:
            print("\nYour creature suffered an infection and unfortunately died...")
            self.is_alive = False
        elif self.boredom >=10:
            self.boredom = 10
            print("\nYour creature is bored and falling asleep z\t...\tz..\tz...")
            self.is_sleeping = True
        elif self.tiredness >= 10:
            self.tiredness = 10
            print("\nYour creature is sleepy and falling asleep")
            self.is_sleeping = True



    def show_menu(creature):
        if creature.is_sleeping:
            choice = input("\nEnter (6) to try and wake up")
            choice = "6"
        else:
            print("\nEnter (1) to eat")
            print("Enter (2) to play")
            print("Enter (3) to sleep")
            print("Enter (4) to take a bath")
            print("Enter (5) to forage for food")
            choice = str(input("What is your choice: "))


        return choice

    def call_action(creature, choice):
        if choice == "1":
            creature.eat()
        elif choice=="2":
            creature.play()
        elif choice=="3":
            creature.sleep()
        elif choice=="4":
            creature.clean()
        elif choice=="5":
            creature.forage()
        elif choice=="6":
            creature.awake()


print("\nWelcome to the Pythonagachi Simulator App")

choice = int(input("Choose the difficult of the level (1-5): "))
if choice > 5:
    choice = 5
elif choice < 1:
    choice = 1

active = True


name = input("What name would you like to five your pet Pythonogachi: ")
my_creature = creature(name)
rounds = 1

while my_creature.is_alive:
    print("\nRound #"+str(rounds))
    my_creature.show_values()
    select = my_creature.show_menu()
    my_creature.call_action(select)


    print("\nRound #"+str(rounds)+" summary")
    my_creature.show_values()
    input("Press ENTER to continue...")

    my_creature.incriment_values(choice)
    my_creature.kill()
    rounds +=1

if not my_creature.is_alive:
    print("R. I. P. I am so sorry to inform about you "+str(my_creature.name)+ " is death...")
    print(str(my_creature.name)+" survived "+str(rounds-1) +".")
play_again = input("Would you like to play again: ?")
if play_again != "y":
    active = False
else:











