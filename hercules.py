from player import Player

class Hercules (Player):
    def __init__(self):
        super (). __init__ ()
        self.name = "Hercules"
    
    def hercules_attack (self):
        self.choose_attack ()

    def hercules_weakness (self):
        if self.defending_against == "bow and arrow":
            self.health -= 40
            print ("You have been hit in the achilles!  And like Achilles you have been gravely wounded!")    
        

        
        

