from game.deck import Deck

class Director:
    # The backbone of the program which controls the sequence of play.

    # Attributes:
    #     deck (class): An instence of Deck
    #     is_playing (boolean): Whether or not the game is being played.
    #     initial_card (int, str): The starting face up card using the Deck method draw.
    #     score (int): The score current score of the player.
    #     guess (str): The players guess of higher or lower
    #     draw (int, str): The face up card that's drawn after the player guesses
    
    def __init__(self):
        # Constructs a new Director.
        # Args: self (Director): an instance of Director.
        
        self.deck = Deck()
        self.is_playing = True
        self.is_playing_suits = False
        self.initial_card = self.deck.draw()
        self.score = 300 # for starting value.
        self.guess = ''
        self.draw = 0
        self.guess_suit = ''
        self.draw_suit = ''

    def start_game(self):
        # Starts the game by running the main game loop.
        # Args: self (Director): an instance of Director.
        
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        # Asks the player to guess if the next card will be higher or lower.
        # Args: self (Director): An instance of Director.
        
        suits = input('Do you want to play with suits? [y/n] ')
        self.is_playing_suits = (suits == "y")
       
        print(f"\nThe card is: {self.initial_card}")
        self.guess = input("Higher or lower? [h/l] ")
        self.draw = self.deck.draw()
        
        if self.is_playing_suits == True:
            self.guess_suit = input('Spade, clover, heart, or diamond? \n[s/c/h/d] ')
            self.draw_suit = self.deck.suit_selector()
    
    def do_updates(self):
        # Updates the player's score.
        # Args: self (Director): An instance of Director.
        
        print(f"Your card is: {self.draw} {self.draw_suit}") 
    
        if self.guess == "h" and self.draw >= self.initial_card:
            self.score += 100
        elif self.guess == "l" and self.draw <= self.initial_card:
            self.score += 100
        else:
            self.score -= 75
        
        if self.score <= 0:
            self.is_playing = False
                           
    def do_outputs(self):
        # Displays the players score and asks if they want to play again. 
        # Args: self (Director): An instance of Director.
        
        if not self.is_playing:
            return
        
        print(f"Your score is: {self.score}\n")
        play_again = input("Play again? [y/n] ")
              
        if play_again == 'n':
            self.is_playing = False
        else:
            self.initial_card = self.draw
       

        
        
