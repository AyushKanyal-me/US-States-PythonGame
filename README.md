#US States Guessing Game

Welcome to the US States Guessing Game! This interactive Python game challenges you to guess all 50 US states using Turtle graphics and the pandas library. It’s a fun and educational way to test your knowledge of US geography.

**Features**

Interactive Map: A visual representation of the US where you can guess the names of the states.
Real-Time Feedback: Receive instant feedback on whether your guess is correct.
Exit Feature: Type "exit" to end the game, and any states you haven't guessed yet will be saved to a separate CSV file.

**Installation**

To get started, you'll need to have Python installed on your computer. You will also need to install the required libraries. Follow these steps:

1. Clone the Repository
```bash

git clone https://github.com/yourusername/us-states-guessing-game.git
cd us-states-guessing-game
```
2. Install Dependencies
You can install the required libraries using pip. Run:

```bash
pip install turtle pandas
```

**Usage**

1. Run the Game
In your terminal or command prompt, navigate to the directory containing the game file and execute:

```bash

python main.py
```
2. Playing the Game
A map of the US will appear, and you will be prompted to enter the name of a state.
Type the name of a state and press Enter.
If your guess is correct, the state will be marked on the map.
If your guess is incorrect, you can try again.
3. Using the Exit Feature
If you wish to end the game before guessing all the states, type "exit" as your input.
The game will terminate, and a CSV file named missed_states.csv will be created in the project directory.
This CSV file will contain a list of all the states you did not guess during the game.
Typing "exit" at any time during the game will:
Save Missed States: All states that have not been guessed will be saved in a file named states_to_learn.csv.csv.

**Contribution**

Feel free to fork the repository, make improvements, and submit pull requests. Your contributions to enhancing the game are greatly appreciated!

Contact

If you have any questions or suggestions, please open an issue on the GitHub repository or contact me directly at ayush.kanyal04@gmail.com.

Happy guessing!

