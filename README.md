# Battle-fleets

## Description
Battle-fleets is a classic battleship game designed to provide users with an engaging and enjoyable gaming experience. Whether you're a seasoned player or new to the game, Battle-fleets offers a fun way to challenge your strategic skills against either an AI opponent or another player.

[Play Battle-fleets](https://ciproject3-1a2d8b8a54cb.herokuapp.com/)

## Table of Contents
1. [Introduction](#introduction)
2. [Design](#design)
3. [Features](#features)
4. [Testing](#testing)
5. [Exception handling](#exceptions)
6. [Deployment](#deployment)
7. [Bugs and Fixes](#bugs-and-fixes)
8. [Resubmission Requirements and Completions](#resubmission-requirements-and-completions)
9. [Value to End Users](#value-to-end-users)
10. [PEP8 Validator](#pep8-validator)
11. [Sources and Credits](#sources-and-credits)

## Introduction
Battle-fleets is a web-based battleship game that offers single-player and two-player modes, customizable settings, and real-time feedback. This README provides an overview of the project's design, features, testing, deployment process, bug fixes, and sources.

## Design
The design of Battle-fleets focuses on simplicity, intuitiveness, and visual appeal. The game interface is designed to be easy to navigate, with clear instructions and feedback to guide the player through each step of the game.

## Features
### Key Features:
- **Player vs AI:** Challenge the computer in a single-player mode.
- **Player vs Player:** Compete against a friend in a two-player mode.
- **Customizable Settings:** Adjust game parameters such as board size and ship placement.
- **Real-time Feedback:** Receive immediate feedback on hits, misses, and game progress.
- **Score Tracking:** Keep track of scores and performance over multiple game sessions.

### Future Features (Planned):
- **Online Multiplayer:** Enable online multiplayer functionality for users to play against friends or random opponents.
- **Advanced AI:** Implement more sophisticated AI algorithms to provide a more challenging opponent.
- **Leaderboard:** Introduce a global leaderboard to track high scores and player rankings.
- **Customizable Themes:** Allow users to customize the game's appearance with different themes and backgrounds.

## Testing
### Browser Testing:
Battle-fleets has been extensively tested on various web browsers including Chrome, Firefox, Safari, Ecosia, and Edge to ensure compatibility and optimal performance across different platforms.

| Browser | Layout + Functionality |
|---------|------------------------|
| Chrome  | ✔                      |
| Firefox | ✔                      |
| Safari  | ✔                      |
| Ecosia  | ✔                      |
| Edge    | ✔                      |

### Manual Testing:
- Checked for correct ship placement and alignment.
- Verified AI behavior and difficulty levels.
- Ensured proper handling of user input and error messages.

## Exception handling
The code implements several 'try except' blocks to catch any erroneous or invalid inputs which the end user could accidentally input.

These first 2 screenshots are about the input for the board size.
![first-board-size](assets/readme_Images/board_size_error.png)


## Deployment
Battle-fleets was deployed via Heroku following these steps:
1. Create requirements.txt.
2. Push to GitHub.
3. Sign up/login to Heroku.
4. Create a new app.
5. Set up configuration variables.
6. Add Python and Node.js buildpacks.
7. Connect GitHub repository.
8. Choose deployment method (manual or automatic).
9. Wait for Heroku to build the application.
10. Open the app and enjoy!

## Bugs and Fixes
Several bugs were identified and fixed during development:
- Invalid Syntax on line 241: Separated the parameter into different lines.
- 'DataFrame' object has no attribute 'append': Changed lines 30 and 31 to correct the append attribute.
- Error occurred during gameplay: empty range in randrange(0, -1): Fixed the randrange issue but need further testing.
- Error loading scoreboard module 'pandas' has no attribute 'read': Fixed the attribute error by separating onto different lines.
- Error occurred during gameplay: name 'dsplay_leaderboard' is not defined: Corrected the function name.
- Error occurred during gameplay: 'BattleshipGame' object has no attribute 'display_leaderboard': Unindented lines 27-35.
- Error occurred during gameplay: 'BattleshipGame' object has no attribute 'exit_game': Changed `exit_game` to `exit_function`.
- SyntaxError 'break' outside loop on line 127: Fixed the indentation.
- NameError: name 'main()' is not defined: Defined the 'main()' function.

## Resubmission Requirements and Completions
This is the first resubmission attempt, focusing on improving the following areas:
- Improved exception handling for invalid inputs.
- Enhanced organization and clarity of the README.
- Added screenshots and value proposition for users.
- Documented PEP8 validation results.

## Value to End Users
Battle-fleets provides a sense of enjoyment and challenges the strategic skills and patience of users against a computer program or other players. With customizable settings and real-time feedback, users can immerse themselves in an engaging gaming experience.

## PEP8 Validator
The Python code has been formatted according to the PEP8 style guide. No errors or warnings were found during validation.

## Sources and Credits
- Code Institute's GitHub repository for providing the project template and guidance.
- Spencer Barriball for mentorship and support.
- Pylint for code formatting.
- Code Institute's Python tester for error checking.
