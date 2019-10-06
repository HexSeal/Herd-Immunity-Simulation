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
        metadata = ("Population size: {}\t", "Vacc Percentage {}\t", "Virus Name {}\t", "Mortality Rate: {}\t", "Basic Reproduction Number: {}\n".format(pop_size, vacc_percentage, virus_name, mortality_rate, basic_repro_num))
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

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''
        # TODO: Finish this method. This method should log when a time step ends, and a
        # new one begins.
        # NOTE: Here is an opportunity for a stretch challenge!
        pass

    def test_logger(self):
        assert self.file_name is "logs.txt"