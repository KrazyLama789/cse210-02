from logging import raiseExceptions
import random

class Deck:
    
    def __init__(self):
        self.value = 0
        self.suit = ''
        
    def draw(self):
        roll = random.randint(1,52)
        if roll in range (1,13):
            self.value = roll
            self.suit = '\u2666'
        elif roll in range (14,26):
            self.value = roll - 13
            self.suit = '\u2665'
        elif roll in range (27,39):
            self.value = roll - 26
            self.suit = '\u2663'
        elif roll in range (40,52):
            self.value = roll - 39
            self.suit = '\u2660'
        
        return self.value

        

