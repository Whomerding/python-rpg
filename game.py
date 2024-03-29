from hercules import Hercules
from enemy import Enemy
class Game:
    def __init__(self):
        self.hercules = Hercules ()
        self.enemy = Enemy ()


  
    def welcome (self):
        print ("Welcome to an epic game featuring an amazing heroe, Hercules, as he fights a deadly foe!")
        print (f"Hercules will be facing off against {self.enemy.enemy_name}.")
        
    def attack_phase (self):
        while self.hercules.health > 0 and self.enemy.health > 0:
            self.hercules.choose_attack ()
            self.enemy.defending_against = self.hercules.attack_name_choice
            self.enemy.enemy_attribute ()
            self.enemy.health -= self.hercules.attack_power
            if self.enemy.health < 0:
                self.enemy.health = 0
            print (f"Hercules has chosen to attack with {self.hercules.attack_name_choice}!  {self.enemy.enemy_name} has {self.enemy.health}% health remaining!")
            if self.enemy.health > 0:
                self.enemy.change_attack_random ()
                self.hercules.defending_against = self.enemy.attack_name_choice
                self.hercules.hercules_attribute ()
                self.hercules.health -= self.enemy.attack_power
                if self.hercules.health < 0:
                    self.hercules.health = 0
                print (f"{self.enemy.enemy_name} has attacked with {self.enemy.attack_name_choice}!  Hercules has {self.hercules.health} remaining!")
                
    def declare_victor (self):
        if self.hercules.health > 0:
            print ("Hercules is victorious!!  Congratulations!")
        else:
            print (f"{self.enemy.enemy_name} has defeated the mighty Hercules!  Better luck next time!!")
    
    def play_again (self):
        self.play_again = input ("Would you like to play again? yes or no? \n")
        if self.play_again == "yes":
            self.run_game ()



    def run_game (self):
        self.enemy = Enemy ()
        self.welcome ()
        self.attack_phase ()
        self.declare_victor ()
        self.play_again ()
