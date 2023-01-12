from player import Player

class Hercules (Player):
    def __init__(self):
        super (). __init__ ()
        self.name = "Hercules"
    
    def choose_attack (self):
        self.attack_choice = input ("What attack would you like to choose?")
        

        
        

