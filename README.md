# Battle-fleets

## Description
Battle-fleets is a classic battleship game designed to provide users with an engaging and enjoyable gaming experience. Whether you're a seasoned player or new to the game, Battle-fleets offers a fun way to challenge your strategic skills against either an AI opponent or another player.

View the app [here](https://ciproject3-1a2d8b8a54cb.herokuapp.com/)

## Table of Contents
1. [Design](#design)
2. [Features](#features)
3. [Testing](#testing)
4. [Deployment](#deployment)
5. [Bugs and Fixes](#bugs-and-fixes)
6. [Sources and Credits](#sources-and-credits)

## Design
- The design of Battle-fleets focuses on simplicity, intuitiveness, and visual appeal. 
- The game interface is designed to be easy to navigate, with clear instructions and feedback to guide the player through each step of the game.

## Features
### Key Features:
- Player vs AI: Challenge the computer in a single-player mode.
- Player vs Player: Compete against a friend in a two-player mode.
- Customizable Settings: Adjust game parameters such as [board size](./readme_Images/board_size.png) and [ship placement](./readme_Images/ship_placement.png) rules.
- Real-time Feedback: Receive immediate feedback on hits, misses, and game progress.
- Score Tracking: Keep track of scores and performance over multiple game sessions.

### Future Features:
- Online Multiplayer: Enable online multiplayer functionality for users to play against friends or random opponents.
- Advanced AI: Implement more sophisticated AI algorithms to provide a more challenging opponent.
- Leaderboard: Introduce a global leaderboard to track high scores and player rankings.
- Customizable Themes: Allow users to customize the game's appearance with different themes and backgrounds.
- Finish off the player vs player


## Testing
- There is one error which i will need to debug personally after the course of when the AI hits your ship once, the game ends and the play_again function is run.
### Browser Testing:
Battle-fleets has been tested extensively on various web browsers including Chrome, Firefox, Safari, and Edge to ensure compatibility and optimal performance across different platforms.
| Browser | Layout + Functionality |
| Chrome  |            ✔           |
| Firefox |            ✔           |
| Safari  |            ✔           |
| Ecosia  |            ✔           |
| Edge    |            ✔           |

### Manual Testing:
- Checked for correct ship placement and alignment.
- checked for the CSV file being updated every time a game is completed
- Verified AI behavior and difficulty levels.
- Ensured proper handling of user input and error messages.
## Deployment
The site was deployed via Heroku
- Firstly to create the requirements to help heroku build the application we type "pip3 freeze > requirements.txt"
- next you push what you have done over to github by:
+ typing 'git add .'
+ then 'git commit -m "froze requirements.txt"'
+ then finally typing 'git push'
- after that we open up a browser and search for [heroku](https://www.heroku.com)
- then once we are on the home page we click on the signup button (or the login button if you already have an account)
- Heroku will then send you a confirmation email which you will need to click on the link within that email.
- hopefully if you have done all of the steps correctly you should be taken to the main dashboard
- From the dashboard we click on create new app
- then you enter a name for your project *please note that no two app names will be the same*
- then you click on a drop down box and pick your region
- afterwards you click on create app
- once you click on the create app button you should see a load of headings
- You click on the settings heading
- then scroll (or press the down arrow if you don't have a mouse with you) till you see the config vars section.
+ if you have scrolled to the config vars section you copy and paste your creds.json file into the 'VALUE' field
+ in the KEY field you type in CREDS
+ then you click on add

+ within the KEY section you add the word PORT and in the VALUE field you add 8000 then click add
- Afterwards you then get to scroll down to the buildpacks section to add two buildpacks.
- Click on add buildpack
- then click on python and save changes
- Click on add buildpack again
- then click on node.js and save changes
*Please make sure that python is on the top and node.js is on the bottom*
- Scroll all the way up to the top of the page and click on deploy
- Then there should be a button which says 'Github' click on it
- Then click on the button which says connect to github
- In a search bar (which should appear if you've clicked on connect to github) enter your repository name
- After that click on the search button
- Then you can click connect
- There is now two options either setup automatic deploys or leave it as manual (i prefer to setup automatic deploys)
+ to set up manual deploys you just click deploy branch
*please note you will have to do this every time you want to deploy a newer version of your application*
+ to set up automatic deploys you make sure that the drop down box is set to master *this is underneath choose a branch to deploy*
+ you then click enable automatic deploys
+ finally click deploy branch
- now just sit back and wait for heroku to build the application
- Finally click on the open app button and you can now view the application

## Bugs and fixes
- There is one error which i will need to debug personally after the course of when the AI hits your ship once, the game ends and the play_again function is run.

- **Line 241 Invalid Syntax:** Separated the parameter into different lines.
- **'DataFrame' object has no attribute 'append':** Changed lines 30 and 31 to correct the append attribute.
- **Error occurred during gameplay: empty range in randrange(0, -1):** Fixed the randrange issue but do need to test more to see if error reoccurrs.
- **Error loading scoreboard module 'pandas' has no attribute 'read':** Fixed the attribute error by separating onto different lines.
- **Error occurred during gameplay: name 'dsplay_leaderboard' is not defined:** Corrected the function name (changed `dsplay_leaderboard` to `display_leaderboard`).
- **Error occurred during gameplay: 'BattleshipGame' object has no attribute 'display_leaderboard':** Unindented lines 27-35.
- **Error occurred during gameplay: 'BattleshipGame' object has no attribute 'exit_game':** Changed `exit_game` to `exit_function`.
- **SyntaxError 'break' outside loop on line 127:** Fixed the indentation.
- **NameError: name 'main()' is not defined:** Defined the 'main()' function.
## Sources and Credits
- Code Institute's GitHub repository for providing the project template and guidance.
- Spencer Barriball for his invaluable mentorship and support throughout the development process.
- Pylint to help make the code look more sensible
- Code Institutes python tester to also help check for errors