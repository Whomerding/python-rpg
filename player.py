import random
class Player:
    def __init__(self):
        self.health = 100
        self.attack_name = {"THE FURY OF THE GODS!!!!": 25, "Full on beast mode!": 20, "Loosing your mind up in here! up in here!": 10, "a very heavy rock": 5, "a small horse": 10, "your mama!": 15, "a rabid squirrel": 12}
        self.attack_power = int

    def change_attack_random (self):   
        self.attack_name = random.choice (list(self.attack_name()))
        self.attack_name = random.choice (list (self.attack_name.value()))

    def choose_attack (self):
        self.display_attacks ()
        self.questions_herc_list = ["Mighty Hercules, how do you choose to attack this villanous fiend?", "How do you wish the dispel with this super evil bad guy?", "What attack would you like to use to kick this dudes butt?"]
        self.random_question  = random.choice (self.questions_herc_list)
        self.attack_name = input (self.random_question)
    
    def display_attacks (self):
        for attack in self.attack_name:
            print (attack)