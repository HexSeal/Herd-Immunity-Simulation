from logger import Logger
from person import Person

def test_log_interaction():
    file = Logger('test3.txt')
    person = Person('1', True, None)
    random_person = Person('2', False, None)
    f = open(file.file_name, 'r+')
    f.truncate(0)
    file.log_interaction(person, random_person, None, None, None)
    lines = f.readlines()
    assert lines == ['Interaction logs: \n','1 did not infect 2 because 2 is vaccinated or already sick \n']
    

    file = Logger('test3.txt')
    person = Person('1', True, None)
    random_person = Person('2', False, None)
    f = open(file.file_name, 'r+')
    f.truncate(0)
    file.log_interaction(person, random_person, None, None, True)
    lines = f.readlines()
    assert lines == ['Interaction logs: \n','1 infects 2\n']

    file = Logger('test3.txt')
    person = Person('1', True, None)
    random_person = Person('2', True, None)
    f = open(file.file_name, 'r+')
    f.truncate(0)
    file.log_interaction(person, random_person, None, None, False)
    lines = f.readlines()
    assert lines == ['Interaction logs: \n','1 did not infect 2\n']

def test_log_infection_survival():
    file = Logger('test3.txt')
    person = Person('1', True, None)
    f = open(file.file_name, 'r+')
    f.truncate(0)
    file.log_infection_survival(person, False)
    lines = f.readlines()
    assert lines == ['Infection Survival: \n', '1 survived infection \n']

    file = Logger('test3.txt')
    person = Person('1', True, None)
    f = open(file.file_name, 'r+')
    f.truncate(0)
    file.log_infection_survival(person, True)
    lines = f.readlines()
    assert lines == ['Infection Survival: \n', '1 died from infection \n']


if __name__ == "__main__":
    logger = Logger("test.txt")

    logger.write_metadata(100, 0.9, "Ebola", 0.2, 0.5)
    
    logger.write_metadata(100, 0.3, "Chicken Pox", 0.4, 0.8)