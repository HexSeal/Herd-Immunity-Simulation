import os

class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''
    # TODO: Write a test suite for this class to make sure each method is working
    # as expected.

    # PROTIP: Write your tests before you solve each function, that way you can
    # test them one by one as you write your class.

    def __init__(self, file_name):
        self.file_name = "logs.txt"


    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        metadata = ("Population size: {}\t Vacc Percentage {}\t Virus Name {}\t Mortality Rate: {}\t Basic Reproduction Number: {}\n".format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))
        f = open(self.file_name, "w+")
        f.write(metadata)

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):

        f = open(self.file_name, "a")
        f.write('Interaction Logs: \n')
        if did_infect:
            infect = (str(person._id) + " infects " + str(random_person._id) + "\n")
            f.write(infect)

        elif random_person.is_vaccinated:
            infect = (str(person._id) + ' did not infect ' + str(random_person._id) + " because " + str(random_person._id) + " is vaccinated\n")
            f.write(infect)

        else:
            infect = (str(person._id) + ' did not infect ' + str(random_person._id) + " because " + str(random_person._id) + " is already infected\n")


    def log_infection_survival(self, person, did_die_from_infection):
        f = open(self.file_name, "a")
        f.write('Survived infection: \n')
        if did_die_from_infection == False:
            status = (str(person._id) + ' survived the infection\n')
            f.write(status)

        else:
            status = str(person._id) + ' died from the infection\n'
            f.write(status)

# @github.com/inv0w helped me with this.
    def log_time_step(self, time_step_number, total_dead, current_infected,
        total_infected, newly_infected, dead_this_step):
        time_step_summary = (f"""\
            {'=+'*25}\nTime step {time_step_number} ended\nInfected this time step: {current_infected}\n
            Died this time step: {dead_this_step}\nTotal Population that has been infected = {total_infected}\n
            Total Deaths = {total_dead}\n{'-'*50}\n""")
        #Removes indentation from the string, and reformats it to allign with text file.
        f = open(self.file_name, "a")
        f.write(self.file_name, time_step_summary)
        #If it's the last step, function will not write to file
        if current_infected != 0:
            with open(self.file_name, "a") as logs_f:
                logs_f.write(f"Step {time_step_number + 1}\n\n")

    def test_logger(self):
        assert self.file_name is "logs.txt"