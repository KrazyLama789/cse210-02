from logging import raiseExceptions
import random

class Deck:
    
    def __init__(self):
        self.current = 0
        self.points = 0
        
    def draw(self):
        roll = random.randint(1,52)
        if roll in range (1,13):
            self.value = roll
        elif roll in range (14,26):
            self.value = roll - 13
        elif roll in range (27,39):
            self.value = roll - 13
        elif roll in range (40,52):
            self.value = roll - 13
        else:
            self.value = 0

        
print('\u2666', '\u2665', '\u2663', '\u2660')

