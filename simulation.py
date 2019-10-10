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
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding
        # parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct
        # parameters.
        # Store the array that this method will return in the self.population
        # attribute.
        # TODO: Store each newly infected person's ID in newly_infected
        # attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
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
            virus_name, pop_size, vacc_percentage, initial_infected)
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
        if self.total_dead == self.pop_size:
           return False
        else:
            return True

    def run(self):
        """
        This method should run the simulation until all requirements for ending
        the simulation are met.
        """
        # TODO: Finish this method.  To simplify the logic here, use the helper
        # method
        # _simulation_should_continue() to tell us whether or not we should
        # continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the
        # end of each time step.
        # TODO: Set this variable using a helper
        self._create_population(self.initial_infected)
        time_step_counter = 0
        should_continue = self._simulation_should_continue()
        dead_this_step = 0

        while should_continue:
            # TODO: for every iteration of this loop, call self.time_step() to
            # compute another
            # round of this simulation.
            self.time_step()
            time_step_counter += 1
            current_killcount = self.total_dead
            dead_this_step = self.total_dead - current_killcount

            print('The simulation has ended after',
                  '{time_step_counter} turns.'.format(time_step_counter))

            self.logger.log_time_step(time_step_counter, self.total_dead, self.current_infected, self.total_infected, len(self.newly_infected),
            dead_this_step)
            should_continue = self._simulation_should_continue()
            
    def time_step(self):
        """
        This method should contain all the logic for computing one time step
        in the simulation.
        This includes:
            1. 100 total interactions with a randon person for each infected
            person in the population
            2. If the person is dead, grab another random person from the
            population.
                Since we don't interact with dead people, this does not count
                as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
        """

        # TODO: Finish this method.
        pass

    def interaction(self, person, random_person):
        """
        This method should be called any time two living people are selected
        for an
        interaction. It assumes that only living people are passed in as
        parameters.
        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.
        """
        # Assert statements are included to make sure that only living people
        # are passed
        # in as params
        assert person.is_alive is True
        assert random_person.is_alive is True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0 and 1.  If that number is
        # smaller
        #     than repro_rate, random_person's ID should be appended to
        #     Simulation object's newly_infected array, so that their .infected
        #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.
        pass

    def _infect_newly_infected(self):
        """
        This method should iterate through the list of ._id stored in
        self.newly_infected
        and update each Person object with the disease.
        """

        # TODO: Call this method at the end of every time step and infect each
        # Person.
        # TODO: Once you have iterated through the entire list of
        # self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()