""" This program makes a battleship game"""
import random
import pandas as pd

class battleshipGame:
    """ A class which holds the code for a battleship game """
    def __init__(self, board_size=8, num_ships=5, player_vs_ai=True, difficulty='medium'):
        """ initializes the object with specified parameters
        parameters:
            board_size: sets board size (8 is default)
            num_ships: sets number of ships (5 is default)
            player_vs_ai: whether the player is against AI (True is default)
            difficulty: sets difficulty of the AI (medium is default)
        """
        self.board_size = board_size
        self.num_ships = num_ships
        self.player_vs_ai = player_vs_ai
        self.difficulty = difficulty
        self.board = [['o' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = []
        self.hits = 0
        self.scores_df = pd.DataFrame(columns=['Player', 'Score'])
