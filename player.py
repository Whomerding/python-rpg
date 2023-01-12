import random
class Player:
    def __init__(self):
        self.health = 100
        self.attack_power = random.randint (0, 15)
        self.attack_name = {"attack": "THE FURY OF THE GODS!!!!", "attack": "Full on beast mode!", "attack": "Loosing your mind up in here! up in here!", "attack": "a very heavy rock", "attack": "a small horse", "attack": "your mama!", "attack": "a rabid squirrel"}

    def change_attack_random (self):   
        self.attack_name = random.choice (list(self.attack_name()))

    def choose_attack (self):
        self.display_attacks ()
        self.questions_herc_list = ["Mighty Hercules, how do you choose to attack this villanous fiend?", "How do you wish the dispel with this super evil bad guy?", "What attack would you like to use to kick this dudes butt?"]
        self.random_question  = random.choice (f"{self.questions_herc_list}")
        self.attack_name = input (self.random_question)
    
    def display_attacks (self):
        for x in self.attack_name:
            print (self.attack_name [x])