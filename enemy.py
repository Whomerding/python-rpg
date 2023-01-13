
from player import Player
import random
class Enemy (Player):
    def __init__(self):
        super ().__init__()
        self.enemy_list = ["Hera", "The Cyclops", "The Minotaur", "Modern Life"]
        self.enemy_name = random.choice (self.enemy_list)
        
    """""
    def hera (self):
        if self.enemy_name == "Hera":
            self.health += 5
        if self.attack_name == "THE FURY OF THE GODS!!!!":
            self.health -= 30
            print ("Zeuss stay out of this!!!")
    def cyclops (self):
        if self.enemy_name == "The Cyclops":
            self.health += 3
        if self.attack_name == "a rabid squirrel":
            self.health -= 25
            print ("Ahhhhh my one giant eye has contracted rabies!!!")
    def minotaur (self):
        if self.enemy_name == "The Minotaur":
            self.health += 2
        if self.attack_name == "a small horse":
            self.health -= 20
    def modern_life (self):
        if self.enemy_name == "Modern Life":
            self.health -= 1
        if self.attack_name == "your mama!":
            self.health -= 30
    def enemy_power_weakness (self):
        self.hera ()
        self.cyclops ()
        self.minotaur ()
        self.modern_life ()
"""