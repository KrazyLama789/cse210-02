from game.card import Card


class Director:
    # The backbone of the program which controls the sequence of play.

    # Attributes:
    #     card (class): An instence of Card
    #     is_playing (boolean): Whether or not the game is being played.
    #     initial_card (int, str): The starting face up card using the Card method: draw.
    #     score (int): The score current score of the player.
    #     guess (str): The players guess of higher or lower
    #     draw (int, str): The face up card that's drawn after the player guesses
    #     is_playing_suits (boolean): Whether or not the game is in suits mode.
    #     guess_suit (str): The players guess of suit.
    #     draw_suit (str): The generated suit.
    #     turn_score (int): The turn score earned by correct high low guess.

    def __init__(self):
        # Constructs a new Director.
        # Args: self (Director): an instance of Director.

        self.card = Card()
        self.is_playing = True
        self.initial_card = self.card.draw()
        self.score = 300  # for starting value.
        self.guess = ''
        self.draw = 0
        self.is_playing_suits = False
        self.guess_suit = ''
        self.draw_suit = ''
        self.turn_score = 0

    def start_game(self):
        # Starts the game by running the main game loop.
        # Optional: Asks if they want to play suits mode.
        # Updates the self.is_playing_suits attribute.
        # Args: self (Director): an instance of Director.

        suits = input('\nDo you want to play suits mode? [y/n] ')
        self.is_playing_suits = (suits == "y")

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        # Asks the player to guess if the next card will be higher or lower.
        # Generates a new card.
        # Makes sure the new card isnt the old card.
        # Updates the self.draw with the new card.
        # If suits: If player is playing suits, ask which suit they guess.
        # If suits: Generates a suit, and updates the corrisponding attribute.
        # Args: self (Director): An instance of Director.

        print(f"\nThe card is: {self.initial_card}")
        self.guess = input("Higher or lower? [h/l] ")
        new_card = self.card.draw()
        
        # Varifys new card isnt the same as the previous card.
        while new_card == self.initial_card:
            new_card = self.card.draw()
        self.draw = new_card

        if self.is_playing_suits == True:
            self.guess_suit = input('Diamond, heart, club, or spade? \n[d/h/c/s] ')
            self.draw_suit = self.card.suit_selector()

    def do_updates(self):
        # Updates the player's score.
        # If suits: Doubles the player's turn score, if they guess the right suit.
        # Args: self (Director): An instance of Director.

        print(f"Your card is: {self.draw} {self.draw_suit}")

        if self.guess == "h" and self.draw >= self.initial_card:
            self.turn_score = 100
            self.score += self.turn_score
        elif self.guess == "l" and self.draw <= self.initial_card:
            self.turn_score = 100
            self.score += self.turn_score
        else:
            self.score -= 75
            self.turn_score = 0

        if self.is_playing_suits == True:
            if self.guess_suit == "d" and self.draw_suit == '\u2666':
                self.score += self.turn_score
            elif self.guess_suit == "h" and self.draw_suit == '\u2665':
                self.score += self.turn_score
            elif self.guess_suit == "c" and self.draw_suit == '\u2663':
                self.score += self.turn_score
            elif self.guess_suit == "s" and self.draw_suit == '\u2660':
                self.score += self.turn_score

        if self.score <= 0:
            self.is_playing = False

    def do_outputs(self):
        # Displays the players score and asks if they want to play again.
        # Args: self (Director): An instance of Director.

        if not self.is_playing:
            return

        print(f"Your score is: {self.score}")
        play_again = input("\nPlay again? [y/n] ")

        if play_again == 'n':
            self.is_playing = False
        else:
            self.initial_card = self.draw
