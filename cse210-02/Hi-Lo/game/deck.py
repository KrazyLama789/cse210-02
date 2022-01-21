from logging import raiseExceptions
import random

class Deck:
    
    def __init__(self):
        self.value = 0
        self.suit = ''
        
    def value(self):
        roll = random.randint(1,13)
        self.value = roll

        return self.value
        
    def suite(self):
        roll = random.randint(1,4)
        self.suite = roll

        return self.suite

