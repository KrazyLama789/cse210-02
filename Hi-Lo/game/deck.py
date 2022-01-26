from logging import raiseExceptions
import random

class Deck:
    # class that creates an instance of the deck
    # Draws a random card and applies a random suit to said card via the suit selector method
    # returns data to be used in the director class
    
    def __init__(self): # creates the instance of the deck
        # self.draw
        # self.suit_selector
        self.value = 0
        self.suit = ''
        
    def draw(self): # generate the card numbers and returns it
        self.value = random.randint(1,13)
        return self.value
    

    def suit_selector(self): # method that generates and returns a random suit 
        roll_suit = random.randint(1,4) 

        if roll_suit == 1:
            self.suit = '\033[31m'+'\u2666'+'\033[0m' # Diamond
        elif roll_suit == 2:
            self.suit = '\033[31m'+'\u2665'+'\033[0m' # Heart
        elif roll_suit == 3:
            self.suit = '\033[32m'+'\u2663'+'\033[0m' # Club
        elif roll_suit ==4:
            self.suit = '\033[36m'+'\u2660'+'\033[0m' # Spade
        return self.suit

