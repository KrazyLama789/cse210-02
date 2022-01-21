from game.deck import Deck

# To start with, I've copied the Director file from the dice came that we are allowed to use.

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck (class): An instence of Deck
        is_playing (boolean): Whether or not the game is being played.
        initial_card (int): The starting face up card.
        score (int): The score for one round of play.
        score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = Deck()
        self.is_playing = True
        self.initial_card = self.deck.draw()
        self.score = 300 # for starting value.
        self.guess = ''
        self.draw = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user to self.guess higher or lower.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nThe card is: {self.initial_card}")
        self.guess = input("Higher or lower? [h/l] ")
        
    
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.draw = self.deck.draw()
        print(f"Next card is: {self.draw}") 
    
        if self.guess == "h" and self.draw >= self.initial_card:
            self.score += 100
        elif self.guess == "l" and self.draw <= self.initial_card:
            self.score += 100
        else:
            self.score -= 75
        
        if self.score <= 0:
            self.is_playing = False
                           

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        print(f"Your score is: {self.score}\n")
        play_again = input("Play again? [y/n] ")
              
        if play_again == 'n':
            self.is_playing = False
        else:
            self.initial_card = self.draw
       

        
        
