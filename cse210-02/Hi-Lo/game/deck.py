from logging import raiseExceptions
import random

class Deck:
    
    def __init__(self):
        self.value = 0
        self.suit = ''
        
    
    def draw_card(self):
        #draw card with random number 1-13
        print()
        
    def suit_selector(self): # method that generates and returns a random suit 
        roll_suit = random.randint(1,4) 

        if roll_suit == 1:
            self.suit = '\u2666'
        elif roll_suit == 2:
            self.suit = '\u2665'
        elif roll_suit == 3:
            self.suit = '\u2663'
        elif roll_suit ==4:
            self.suit = '\u2660'
        return self.suit
        
        

        

