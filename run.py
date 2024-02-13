""" This program makes a battleship game"""
import random
import pandas as pd
import time as t

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
        new_data = pd.DataFrame({'Player': [player], 'Score': [score]})
        self.scores_df = pd.concat([self.scores_df, new_data], ignore_index=True)
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
    def load_scores_csv(self,filename="battleship_score.csv"):
        """ 
        loads the dataframe from the CSV file
        """
        try:
            self.scores_df = pd.read(filename)
            print("Scores loaded from CSV file", filename)
        except FileNotFoundError:
            print("Score leaderboard not found starting with an empty board")
        except Exception as e:
            print("Error loading scoreboard", e)
    def place_ships(self):
        """ 
        function to randomly place the ships
        """
        for _ in range(self.num_ships):
            length = random.randint(2,5)
            horizontal = random.choice([True, False])
            if horizontal:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - length)
                for i in range(length):
                    self.board[row][col + i] = 'S'
            else:
                row = random.randint(0, self.board_size - length)
                col = random.randint(0, self.board_size - 1)
                for i in range(length):
                    self.board[row + i][col] = 'S'
            self.ships.append((row,col,length, horizontal))
    def print_board(self,show_ships=False):
        """ 
        prints the game board
        show_ships(bool): whether to reveal ship locations
        """
        print("   " + " ".join(str(i) for i in range(self.board_size)))
        for i in range(self.board_size):
            if not show_ships:
                row = ' '.join(self.board[i])
            else:
                row = ' '.join(['S' if cell == 'S' else 'O' for cell in self.board[i]])
            print(f"{i} | {row}")
    
    def valid_guess(self, row, col):
        """ 
        Checks for a valid guess (within boundaries and not already guessed)
        row (int) = the row index of the guess
        col (int) = the col index of the guess

        returns true if guess is valid false if not
        """
        return (
            0 <= row < self.board_size and
            0 <= col < self.board_size and
            self.board[row][col] != 'X'
        )
    
    def player_guess(self):
        """ 
        takes input for players guess
        returns a tuple which has rows and cols from the guess
        """
        try:
            row = int(input("Enter row number: "))
            col = int(input("Enter col number: "))
            if not self.valid_guess(row,col):
                print("Invalid guess ")
                print("Try again! ")
                return self.player_guess()
            return row,col
        except ValueError:
            print("Invalid input!")
            print("Make sure to enter numbers(integers)")
            return self.player_guess()

    def ai_guess(self, guess_stragety):
        """ 
        does the AI guess
        also returns a tuple of the rows and cols from the guess
        """
        if self.difficulty == 'cheating':
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            return row,col
        elif self.difficulty == 'impossible':
             row, col = self.ai_guess_advanced()
            # choose random cell if probabilities are equal
             return random.randint(0, self.board_size - 1)
             return random.randint(0, self.board_size - 1)
        elif self.difficulty == 'easy':
            row = random.randint(0, self.board_size - 1)
            col = random.randint(0, self.board_size - 1)
            while not self.valid_guess(row, col):
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - 1)
        elif self.difficulty == 'medium':
            row, col = self.ai_guess_random()
            if self.board[row][col] == 'H':
                row, col = self.ai_guess_nearby(row, col)
        else:
            row, col = self.ai_guess_medium()
        return row, col
        return guess_stragety()
    def ai_guess_advanced(self):
        """ 
        Generates AI's guess in a more advanced way
        returns a tuple containing row and col indicies of guess
        """
        if self.hits > 0:
            row, col = self.target_tracking()
        else:
            row, col = self.probability_based()
        return row,col
    def target_tracking(self):
        """ 
        Generates AI guess using tracking
        returning tuple of row and col indicies
        """
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] == 'H':
                    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        x, y = i + dx, j + dy
                        if 0 <= x < self.board_size and 0 <= y < self.board_size:
                            if self.board[x][y] == 'O':
                                return x,y
        return self.ai_guess_random()
    def probability_based(self):
        """ 
        Generates AI guess using probability
        returns a tuple with row n col indicies
        """
        max_prob = max(max(row) for row in self.ai_probabilities)
        for i in range (self.board_size):
            for j in range(self.board_size):
                if self.ai_probabilities[i][j] == max_prob:
                    return i,j
        return self.ai_guess_random()
    def ai_guess_random(self):
        """ 
        makes AI guess randomly
        returns tuple of row and col index of guess
        """
        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)
        return row, col
    
    def play(self):
        """ 
        Starts the game and controls flow of gameplay
        """
        try:
            if self.difficulty == 'impossible':
                print("Welcome to impossible mode!")
                t.sleep(1)
                print("You have no chance of winning")
                return
            
            self.place_ships()
            while self.hits < self.num_ships:
                print("\nPlayers Turn" if self.player_vs_ai else "\nPlayer 1 go")
                self.print_board()
                if self.player_vs_ai:
                    guess_row, guess_col = self.player_guess()
                else:
                    guess_row = self.player_guess()
                    guess_col = self.player_guess()
                if self.board[guess_row][guess_col] == 'S':
                    print("Aye ye hit me battleship!")
                    self.board[guess_row][guess_col] = 'X'
                    self.hits += 1
                else:
                    print("phew you missed!")
                    self.board[guess_row][guess_col] = 'X'
                if self.hits == self.num_ships:
                    print("Congrats! you have sunk all my battleships!")
                    if self.player_vs_ai:
                        player_name = "Player"
                    else:
                        player_name = "Player 1"
                    self.update_scores(player_name, 100)
                    self.display_leaderboard()
                    self.save_scores_csv()

                if self.player_vs_ai:
                    print("\nAI turn")
                    ai_guess_row, ai_guess_col = self.ai_guess(
                        self.ai_guess_advanced
                        )
                    print(f"AI Guesses: {ai_guess_row}, {ai_guess_col}")
                    if self.board[ai_guess_row][ai_guess_col] == 'S':
                        print("AI has been hit!")
                        self.board[ai_guess_row][ai_guess_col] = 'X'
                        self.hits += 1
                    else:
                        print("AI has missed! ")
                        t.sleep(1)
                        print("You may have another go!")
        except KeyboardInterrupt:
            print("\n game interrpted by user!")
        except Exception as e:
            print("Error occurred during gameplay:", e)
if __name__ == "__main__":
    try:
        print("Welcome to battleships!")
        board_size = int(input("enter the board size (default is 8): ") or 8)
        num_ships = int(input("Enter number of ships (default is 5): ") or 5)
        player_vs_ai = input("Play against AI? (y/n default is yes): ").lower() !="n"
        if player_vs_ai:
            difficulty = input("""Choose difficulty 
            (easy/medium/hard/cheating/impossible, default is medium):""")
            difficulty.lower() or 'medium'
            game = battleshipGame(board_size,num_ships,player_vs_ai,difficulty)
            game.play()
        else:
            difficulty = 'medium'
            game = battleshipGame(board_size,num_ships,player_vs_ai,difficulty)
            game.load_scores_csv()
            game.play()
    except Exception as e:
        print("Unexpected error occurred:", e)