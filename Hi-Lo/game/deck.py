from logging import raiseExceptions
import random

class Deck:
    
    def __init__(self):
        self.value = 0
        self.suit = ''
        
    def value(self): # generate the card numbers and returns it
        self.value = random.randint(1,13)
        return self.value
    

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
      
        

