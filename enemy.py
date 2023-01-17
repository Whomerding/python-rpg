
from player import Player
import random
class Enemy (Player):
    def __init__(self):
        super ().__init__()
        self.enemy_list = ["Hera", "The Cyclops", "The Minotaur", "Modern Life"]
        self.enemy_name = random.choice(self.enemy_list)
    
    def hera (self):
        if self.enemy_name == "Hera" and self.health == 100:
            self.health += 25
        if self.enemy_name == "Hera" and self.defending_against == "a very heavy rock":
            print ("A small pebble can not hurt Hera!")
            self.health += 5
        if self.enemy_name == "Hera" and self.defending_against == "THE FURY OF THE GODS!!!!":
            self.health -= 30
            print ("Zeuss stay out of this!!!")
    def cyclops (self):
        if self.enemy_name == "The Cyclops" and self.health == 100:
            self.health += 15
        if self.enemy_name == "The Cyclops" and self.defending_against == "Loosing your mind up in here! up in here!":
            self.health += 14
            print ("Losing your mind has no effect on the Cyclops!")
        if self.enemy_name == "The Cyclops" and self.defending_against == "a rabid squirrel":
            self.health -= 25
            print ("Ahhhhh my one giant eye has contracted rabies!!!")
    def minotaur(self):
        if self.enemy_name == "The Minotaur" and self.health == 100:
            self.health += 10
        if self.enemy_name == "The Minotaur" and self.defending_against == "a rabid squirrel":
            self.health += 12
            print ("The Minotaur is unphased by the rabid squirrel!")
        if self.enemy_name == "The Minotaur" and self.defending_against == "a small horse":
            self.health -= 20
            print ("The small horse has distracted and infatuated the minotaur!")
    def modern_life (self):
        if self.enemy_name == "Modern Life" and self.health == 100:
            self.health -= 5
        if self.enemy_name == "Modern Life" and self.defending_against == "THE FURY OF THE GODS!!!!":
            print ("Your old gods have no power over Modern Life!!")
            self.health += 25
        if self.enemy_name == "Modern Life" and self.defending_against == "your mama!":
            self.health -= 30
            print ("Your Mama is mighty!!")
    
    def enemy_attribute (self):
        self.hera ()
        self.cyclops ()
        self.minotaur ()
        self.modern_life ()
    
    