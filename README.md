# Hangman Word Game

A classic hangman-style word guessing game implemented in Python. Players guess letters to reveal a secret food-themed word within a limited number of attempts.

## Features

- **Random Word Selection**: Choose from a curated list of food words (pizza, burger, sushi, waffle, fish, steak)
- **Interactive Gameplay**: Console-based interface with real-time feedback
- **Input Validation**: Robust validation prevents invalid inputs and duplicate guesses
- **Win/Loss Detection**: Clear win and loss conditions with appropriate messaging
- **Turn Tracking**: 6 attempts to guess the word correctly

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone or download this repository
3. Navigate to the project directory

## Usage

Run the game from the command line:

```bash
python main.py
```

Follow the on-screen prompts to guess letters. The game will display:
- The current state of the word (with blanks for unguessed letters)
- Number of turns remaining
- Feedback on correct/incorrect guesses

## Game Rules

1. A random food word is selected at the start of each game
2. You have 6 turns to guess the word
3. Guess one letter at a time
4. Correct guesses reveal the letter in the word
5. Incorrect guesses reduce your remaining turns
6. Win by guessing all letters before running out of turns
7. Lose if you exhaust all 6 turns without guessing the word

## Testing

Run the test suite to verify functionality:

```bash
python test_game.py
```

The test suite includes:
- Word selection validation
- Display functionality testing
- Input validation testing

## Project Structure

- `main.py` - Main game logic and console interface
- `test_game.py` - Unit tests using Python's unittest framework
- `MY_NOTES.md` - Development notes and architecture documentation
- `REPORT.md` - Project completion report and requirements verification

## Requirements

- Python 3.x
- No external dependencies (uses only standard library modules: `random`, `string`, `unittest`)

## Future Enhancements

- Auto-play mode (currently in development)
- Expanded word list
- Difficulty levels
- Score tracking
- GUI interface

## License

This project is developed as part of a lab assignment.