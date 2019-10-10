from person import Person
from virus import Virus
from logger import Logger
from simulation import Simulation

def test_simulation_init():
    virus = Virus("Ebola", .3, .8)
    sim = Simulation(35000, .9, virus, 1)
    assert sim.pop_size == 35000
    assert sim.vacc_percentage == .9
    assert sim.virus.name == "Ebola"
    assert sim.initial_infected == 1

def test_create_population():
    virus = Virus("Ebola", .3, .8)

    person1 = Person(0, is_vaccinated=False, infection=virus)
    person2 = Person(1, is_vaccinated=True, infection=None)
    person3 = Person(2, is_vaccinated=False, infection=virus)

    assert person1.infection == virus
    assert person2.infection is None
    assert person2.is_alive is True
    assert person2.is_vaccinated is True
    assert person3.infection is None
    assert person3.is_alive is True
    assert person3.is_vaccinated is False

def test_is_population_dead():
    virus = Virus("Ebola", .3, .8)
    sim = Simulation(10, .5, virus, 1)
    assert sim._simulation_should_continue is True

    for person in sim.population:
        person.is_alive = False
    assert sim._simulation_should_continue is False

def test_simulation_should_continue():
    virus = Virus("Ebola", .3, .8)
    sim = Simulation(100, 100, virus)
    person1 = Person(1, True)
    person2 = Person(2, False)
    sim.population = [person1, person2]
    assert sim._simulation_should_continue() is True

    person1.is_alive = False
    person2.is_alive = False
    assert sim._simulation_should_continue() is False

def test_run():
    pass

def test_get_infected():
    pass

def test_interaction():
    pass

def test_time_step():
    pass

def test_infect_newly_infected():
    pass