import random
import math
import tkinter

class Simulation():
    def __init__(self):
        self.day_number = 1
        #the beginner number of days

        print("To simulate an epidemic outbreak, we must know the population size.")
        self.population_size = int(input("---Enter the population size: "))
        root = math.sqrt(self.population_size)
        if int(root +.5)**2 != self.population_size:
            round(root,0)
            self.grid_size = int(root)
            self.population_size = self.grid_size**2
            print("\nRounding population size to "+str(self.population_size)+ "for visual purposes.")
        else:
            self.grid_size = int(math.sqrt(self.population_size))


        print("\nWe must first start by infecting a portion of the population.")
        self.infection_size = float(input("---Enter the percentage (0-100) of the population to initially infect: "))
        self.infection_size = self.infection_size/100

        print("\nWe must know the risk a person has to contact the disease when exposed.")
        self.infection_probability = int(input("--Enter the probability (0-100) that a person gets infected when exposed to the disease: "))

        print("\nWe must know how long the infection will last when exposed.")
        self.infection_duration = int(input("--Enter the duration (in days) of the infection: "))

        print("\nWe must know the mortality rate of those infected.")
        self.mortality_rate = int(input("--Enter the mortality rate (0-100) of the infection: "))

        print("\nWe must know how long to run the simulation.")
        self.sim_days = int(input("--Enter the number of days to simulate: "))


class Person():
    def __init__(self):
        self.is_infected = False
        self.is_dead = False
        self.days_infected = 0

    def infect(self,sim):
        chance_to_become_infected = random.randint(0,100)
        if chance_to_become_infected < sim.infection_probability:
            self.is_infected = True

    def heal(self):
        self.is_infected = False
        self.days_infected = 0

    def die(self):
        self.is_dead = True

    def update(self,sim):
        if self.is_dead == False:
            if self.is_infected == True:
                self.days_infected +=1
                integer = random.randint(0,100)
                if integer < sim.mortality_rate:
                    self.die()
                elif self.days_infected == sim.infection_duration:
                    self.heal()


class Population():
    def __init__(self, sim):
        self.population = []


        for i in range(sim.grid_size):
            row = []
            for j in range(sim.grid_size):
                person = Person()
                row.append(person)
            self.population.append(row)



    def initial_infection(self, sim):
        infected_count = int(round(sim.infection_size * sim.population_size,0))

        infections = 0
        while infections < infected_count:

            x = random.randint(0, sim.grid_size - 1)
            y = random.randint(0, sim.grid_size - 1)

            if not self.population[x][y].is_infected:
                self.population[x][y].is_infected = True
                self.population[x][y].days_infected =1
                infections +=1

    def spread_infection(self, sim):
        for i in range(sim.grid_size):
            for j in range(sim.grid_size):
                if self.population[i][j].is_dead == False:
                    if i == 0:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(sim)
                        elif j== sim.grid_size-1:
                            if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(sim)

                        else:
                            if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected:
                                self.population[i][j].infect(sim)
                    elif i == sim.grid_size-1:
                        if j ==0:
                            if self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(sim)
                            elif j == sim.grid_size-1:

                                if self.population[i][j-1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(sim)
                            else:
                                if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(sim)

                    else:
                        if j == 0:
                            if self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                self.population[i][j].infect(sim)
                            elif j==sim.grid_size-1:
                                if self.population[i][j-1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                    self.population[i][j].infect(sim)
                                else:
                                    if self.population[i][j-1].is_infected or self.population[i][j+1].is_infected or self.population[i+1][j].is_infected or self.population[i-1][j].is_infected:
                                        self.population[i][j].infect(sim)

    def update(self, sim):
        sim.day_number +=1
        for row in self.population:
            for person in row:
                person.update(sim)

    def display(self,sim):
        total_infected = 0
        total_death_count = 0
        for x in self.population:
            for y in x:
                if y.is_infected:
                    total_infected += 1
                    if y.is_dead:
                        total_death_count += 1
        infected_percent = round((total_infected/sim.population_size)*100,4)
        death_percent = round((total_death_count/sim.population_size)*100,4)
        print("-----Day #"+str(sim.day_number)+"-----")
        print("Percentage of Population Infected: "+str(infected_percent)+"%")
        print("Percent of Population Dead: "+str(death_percent)+"%")
        print("Total People Infected: "+str(total_infected)+"/"+str(sim.population_size))
        print("Total Deaths: "+str(total_death_count)+"/"+str(sim.population_size))


def graphics(sim,population, canvas):
    square_dimension = 600//sim.grid_size
    for i in range(sim.grid_size):
        y = i * square_dimension
        for j in range(sim.grid_size):
            x = j*square_dimension
            if population.population[i][j].is_dead:
                canvas.create_rectangle(x,y, x+square_dimension, y+square_dimension, fill='red')
            else:

                if population.population[i][j].is_infected:
                    canvas.create_rectangle(x,y, x+square_dimension,y+square_dimension, fill='yellow')
                else:
                    canvas.create_rectangle(x,y, x+square_dimension,y+square_dimension, fill='green')

sim = Simulation()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

sim_window = tkinter.Tk()
sim_window.title("Epidemic Outbreak")

sim_canvas = tkinter.Canvas(sim_window, width = WINDOW_WIDTH, height = WINDOW_HEIGHT, bg="lightblue")
sim_canvas.pack(side = tkinter.LEFT)

population = Population(sim)

population.initial_infection(sim)
population.display(sim)

input("Press enter to being the simulation.")

for x in range(1,sim.sim_days):
    population.spread_infection(sim)
    population.update(sim)
    population.display(sim)
    graphics(sim,population,sim_canvas)
    sim_window.update()
    if x != sim.sim_days-1:
                sim_canvas.delete("all")






















