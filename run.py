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
    def update_scores(self, player, score):
        """ 
        updates the dataframe with the scores and player name
        arguments:
            player(str)
            score(int) - The players score
        """
        self.scores_df = self.scores_df.append({'Player' : player, 'Score' : score}, ignore_index=True)

    def display_leaderboard(self):
        """ 
        Shows the leaderboard with top players and their scores
        """
        try:
            leaderboard = self.scores_df.sort_values(by='Score', ascending=False).head(10)
            print("Leaderboard:\n")
            print(leaderboard)
        except Exception as e:
            print("Error displaying the leaderboard: ", e)
    def save_scores_csv(self,filename="battleship_score.csv"):
        """ 
        Saves the scores to the csv file

        filename (str) = the filename which will save the scores dataframe
        """
        try:
            self.scores_df.to_csv(filename, index=False)
            print("Scores Saved to CSV:", filename)
        except Exception as e:
            print("Error Saving scores to CSV:", e)
            