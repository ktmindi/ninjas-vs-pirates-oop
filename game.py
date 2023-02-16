from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
jack_sparrow.show_stats()

class Game:
    print("The Ultimate Battle of Pirates versus Ninjas will now begin!!")
    name = input("What is your name Human?")
    team = input("Choose your Team - Pirates or Ninjas")
    
    def __init__(self):
        name1 = input("What is your name Player 1?")
        name2 = input("What is your name Player 2?")