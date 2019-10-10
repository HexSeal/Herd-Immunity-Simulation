import random, sys
import sys
from person import Person
from logger import Logger
from virus import Virus
import numpy as np
random.seed(42)

''' Used starter code from https://github.com/Evansdava/Herd-Immunity/blob/master/starter_code/simulation.py'''

class Simulation(object):
    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        self.logger = Logger("logs.txt")
        self.population = []  # List of Person objects
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.total_dead = 0  # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            self.virus.name, pop_size, vacc_percentage, initial_infected)
        self.newly_infected = []

    def _create_population(self, initial_infected):
        # borrowed this idea from github.com/inv0w
        num_of_vaccinated = int(self.vacc_percentage * self.pop_size)
        vacc_seeding = np.random.choice(range(1, (self.pop_size) + 1), num_of_vaccinated, replace=False)
        virus_seeding = np.random.choice(range(1, (self.pop_size) + 1), initial_infected, replace=False)

        for i in range(self.pop_size):
            person = Person(i+1, False, None)
            self.population.append(person)
            if person._id in vacc_seeding: person.is_vaccinated = True
            if person._id in virus_seeding:
                self.newly_infected.append(person._id)
                self.current_infected += 1
                person.infection = self.virus

    def _simulation_should_continue(self):
        for person in self.population:
            if person.is_alive:
                if person.infection == self.virus:
                    return True
        return False

    def run(self):
        """
        This method should run the simulation until all requirements for ending
        the simulation are met.
        """
        self._create_population(self.initial_infected)
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        dead_this_step = 0

        while should_continue:
            self.time_step()
            time_step_counter += 1
            current_killcount = self.total_dead
            dead_this_step = self.total_dead - current_killcount

            self.logger.log_time_step(time_step_counter, self.total_dead, self.current_infected, self.total_infected, len(self.newly_infected),
            dead_this_step)
            should_continue = self._simulation_should_continue()

        print('The simulation has ended after',
                '{} turns.'.format(time_step_counter))
            
    def time_step(self):
        num_interactions = 0
        for person in self.population:
            if person.infection == self.virus and person.is_alive:
                while num_interactions < 100:
                    random_person = random.choice(self.population)
                    if random_person.is_alive and random_person._id != person._id:
                        num_interactions += 1
                        self.interaction(person, random_person)
                    else:
                        random_person = random.choice(self.population)

                num_interactions =  0

        if person.did_survive_infection():
            self.logger.log_infection_survival(person, True)
            
        self._infect_newly_infected()


    def interaction(self, person, random_person):
        assert person.is_alive is True
        assert random_person.is_alive is True
        random_num = random.random()
        if random_num < self.virus.repro_rate:
            self.newly_infected.append(random_person._id)
            self.logger.log_interaction(person, random_person)
            
        else:
            self.logger.log_interaction(person, random_person)

    def _infect_newly_infected(self):
        """
        This method should iterate through the list of ._id stored in
        self.newly_infected
        and update each Person object with the disease.
        """
        for person in self.population:
            if person._id in self.newly_infected:
                person.infection == self.virus
        self.newly_infected = []
        pass

def test_run_function():
    virus = Virus("Ebola", 0.25, 0.70)
    sim = Simulation(100, 0.50, virus, 1)
    sim.run()

if __name__ == "__main__":
    test_run_function()