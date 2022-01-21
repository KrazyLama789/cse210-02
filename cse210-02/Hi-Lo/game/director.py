from game.deck import Deck

# To start with, I've copied the Director file from the dice came that we are allowed to use

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        deck (class): An instence of Deck
        is_playing (boolean): Whether or not the game is being played.
        current_card (int): The current face up card.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.deck = Deck()
        self.is_playing = True
        self.current_card = 0
        self.score = 0
        self.total_score = 300 # for starting value.

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
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        draw_card = input("Draw a card? [y/n] ") 
        self.is_playing = (draw_card == "y")
        
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        self.score = 0

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score
        
        

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print(f"You drew: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing = (self.score > 0)
        
