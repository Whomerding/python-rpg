import random
class Player:
    def __init__(self):
        self.health = 100
        self.attack_power = random.randint (0, 15)
        self.attack_name = {"attack": "THE FURY OF THE GODS!!!!", "attack": "Full on beast mode!", "attack": "Loosing your mind up in here! up in here!", "attack": "a very heavy rock", "attack": "a small horse", "attack": "your mama!", "attack": "a rabid squirrel"}

    def change_attack (self):   
        self.attack_name = random.choice (list(self.attack_name()))
