"""This program makes a battleship game"""
import time as t
import random
import pandas as pd

class BattleshipGame:
    """A class which holds the code for a battleship game"""

    def __init__(self, board_size=8, num_ships=5, player_vs_ai=True, DIFFICULTY='medium'):
        """Initializes the object with specified parameters"""
        self.board_size = max(1, board_size)  # Ensure board size is at least 1
        self.num_ships = max(1, num_ships)  # Ensure number of ships is at least 1
        self.player_vs_ai = player_vs_ai
        self.DIFFICULTY = DIFFICULTY.upper()  # Ensure difficulty is in uppercase
        self.board = [['o' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = [] # sets ships to an empty array
        self.hits = 0 # sets hits to 0
        self.scores_df = pd.DataFrame(columns=['Player', 'Score']) # makes a dataframe with columns player and score

    def update_scores(self, player, score):
        """Updates the dataframe with the scores and player name"""
        # makes the dataframe into a new variable
        new_data = pd.DataFrame({'Player': [player], 'Score': [score]})
        # sets the original variable to combine that and new_data
        self.scores_df = pd.concat([self.scores_df, new_data], ignore_index=True)

    def display_leaderboard(self):
        """Shows the leaderboard with top players and their scores"""
        # Tries this block of code
        try:
            leaderboard = self.scores_df.sort_values(by='Score', ascending=False).head(10)
            print("Leaderboard:\n")
            print(leaderboard)
        except Exception as e:
            print("Error displaying the leaderboard: ", e)

    def save_scores_csv(self, filename="battleship_score.csv"):
        """Saves the scores to the CSV file"""
        try:
            self.scores_df.to_csv(filename, index=False)
            print("Scores Saved to CSV:", filename)
        except Exception as e:
            print("Error Saving scores to CSV:", e)

    def load_scores_csv(self, filename="battleship_score.csv"):
        """Loads the dataframe from the CSV file"""
        try:
            self.scores_df = pd.read_csv(filename)
            print("Scores loaded from CSV file", filename)
        except FileNotFoundError:
            print("Score leaderboard not found starting with an empty board")
        except Exception as e:
            print("Error loading scoreboard", e)

    def place_ships(self):
        """ Helps to place the ships in random spots on board """
        for _ in range(self.num_ships):
            length = random.randint(2, 5)
            horizontal = random.choice([True, False])
            if horizontal:
                row = random.randint(0, self.board_size - 1)
                col = random.randint(0, self.board_size - length)  # Adjusted range
                for i in range(length):
                    self.board[row][col + i] = 'S'
            else:
                row = random.randint(0, self.board_size - length)  # Adjusted range
                col = random.randint(0, self.board_size - 1)
                for i in range(length):
                    self.board[row + i][col] = 'S'
            self.ships.append((row, col, length, horizontal))


    def print_board(self, show_ships=False):
        """Prints the game board"""
        print("   " + " ".join(str(i) for i in range(self.board_size)))
        for i in range(self.board_size):
            if not show_ships:
                row = ' '.join(self.board[i])
            else:
                row = ' '.join(['S' if cell == 'S' else 'O' for cell in self.board[i]])
            print(f"{i} | {row}")

    def valid_guess(self, row, col):
        """Checks for a valid guess (within boundaries and not already guessed)"""
        return (
            0 <= row < self.board_size and
            0 <= col < self.board_size and
            self.board[row][col] != 'X'
        )

    def player_guess(self):
        """Takes input for the player's guess.
        Returns a tuple with the row and column indices from the guess."""
        try:
            # checks for inputs as an integer
            row = int(input("Enter row number: \n"))
            col = int(input("Enter col number: \n"))
            # if inputs are not returned from function then
            if not self.valid_guess(row, col):
                # output this and return a function
                print("Invalid guess. Please try again.")
                return self.player_guess()
            # returns the row, col
            return row, col
            # unless this error happens then
        except ValueError:
            # prints this
            print("Invalid input! Make sure to enter integers.")
            return self.player_guess()

    def ai_guess(self):
        """Makes the AI guess and returns a tuple of the rows and columns from the guess."""
        row = random.randint(0, self.board_size - 1)
        col = random.randint(0, self.board_size - 1)
        return row, col

    def play(self):
        """Starts the game and controls the flow of gameplay"""
        try:
            self.place_ships()
            while self.hits < self.num_ships:
                print("\nPlayers Turn" if self.player_vs_ai else "\nPlayer 1 go")
                self.print_board()
                if self.player_vs_ai:
                    guess_row, guess_col = self.player_guess()
                else:
                    guess_row, guess_col = self.player_guess()
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
                        player_name = input("Please enter your name now! \n")
                    else:
                        player_name = "Player 1"
                    self.update_scores(player_name, 100)
                    self.display_leaderboard()
                    self.save_scores_csv()
                    # Ask user if they want to play again or exit
                    self.play_again_prompt()

                if self.player_vs_ai:
                    print("\nAI turn")
                    ai_guess_row, ai_guess_col = self.ai_guess()
                    print(f"AI Guesses: {ai_guess_row}, {ai_guess_col}")
                    if self.board[ai_guess_row][ai_guess_col] == 'S':
                        print("AI has hit your ship!")
                        self.board[ai_guess_row][ai_guess_col] = 'X'
                        self.hits += 1
                    else:
                        print("AI has missed! ")
                        t.sleep(1)
                        print("You may have another go!")
        except KeyboardInterrupt:
            print("\n Game interrupted by user!")
        except Exception as e:
            print("Error occurred during gameplay:", e)
    
    def exit_function(self):
        """ Exits out the program. """
        print("Well goodbye!")
        sys.exit(0)

    def play_again_prompt(self):
        """Ask user if they want to play again or exit."""
        while True:
            play_again = input("Do you want to play again? (yes/no): ").strip().lower()
            if play_again in ['yes', 'y']:
                print("Starting a new game...")
                # Restart the game
                self.__init__(self.board_size, self.num_ships, self.player_vs_ai, self.DIFFICULTY)
                self.play()
                break
            elif play_again in ['no', 'n']:
                self.exit_game()
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    try:
        print("Welcome to battleships!")
        while True:
            try:
                board_size = int(input("Enter the board size (default is 8): \n") or 8)
                if board_size <= 0:
                    raise ValueError("Board size must be a positive integer greater than 0.")
                break
            except ValueError as ve:
                print("Invalid input:", ve)

        while True:
            try:
                num_ships = int(input("Enter number of ships (default is 5): \n") or 5)
                if num_ships <= 0 or num_ships > board_size:
                    raise ValueError(f"Number of ships must be a positive integer less than or equal to {board_size}.")
                break
            except ValueError as ve:
                print("Invalid input:", ve)

        player_vs_ai = input("Play against AI? (y/n default is yes): \n").lower() != "n"
        if player_vs_ai:
            while True:
                DIFFICULTY = input("""Choose difficulty
                (easy/medium/hard/cheating/impossible, default is medium): \n""")
                DIFFICULTY = DIFFICULTY.lower() or 'medium'
                if DIFFICULTY in ['easy', 'medium', 'hard', 'cheating', 'impossible']:
                    break
                else:
                    print("Invalid difficulty level. Please choose from the given options.")

            game = BattleshipGame(board_size, num_ships, player_vs_ai, DIFFICULTY)
            game.play()
        else:
            DIFFICULTY = 'medium'
            game = BattleshipGame(board_size, num_ships, player_vs_ai, DIFFICULTY)
            game.load_scores_csv()
            game.play()
    except Exception as e:
        print("Unexpected error occurred:", e)
