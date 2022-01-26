from logging import raiseExceptions
import random

class Card:
    # class that creates an instance of the deck
    # Draws a random card and applies a random suit to said card via the suit selector method
    # returns data to be used in the director class
    
    def __init__(self): # creates the instance of the deck
        self.draw()
        self.suit_selector()
        
    def draw(self): # generate the card numbers and returns it
        self.value = random.randint(1,13)
        return self.value
    

    def suit_selector(self): # method that generates and returns a random suit 
        roll_suit = random.randint(1,4) 

        if roll_suit == 1:
            self.suit = '\u2666' # Diamond
        elif roll_suit == 2:
            self.suit = '\u2665' # Heart
        elif roll_suit == 3:
            self.suit = '\u2663' # Club
        elif roll_suit ==4:
            self.suit = '\u2660' # Spade
        return self.suit

