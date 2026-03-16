# Hangman Game - Architecture Summary

## Game States

1. **INIT**: `pick_word()` selects a random word; initialize `guessed_letters` (empty list) and `turns_left` (6)
2. **LOOP**: Core game loop in `play_game()` — display word state, prompt for input, validate, evaluate guess, update state
3. **WIN**: All letters in `secret_word` are present in `guessed_letters` (checked via `all()`)
4. **LOSS**: `turns_left` reaches 0 with game still ongoing
5. **Auto**:  get_auto_guess(guessed_letters): is going to use the guessed_letters to find the next letter

## Core Variables

| Variable | Type | Purpose |
|----------|------|---------|
| `secret_word` | str | The target word to guess |
| `guessed_letters` | list | Tracks all player guesses (prevents duplicates) |
| `turns_left` | int | Remaining attempts (decrements on wrong guess) |
| `guess` | str | Single validated letter input from player |

## Function Responsibilities

- **`pick_word()`**: Returns random word from word list
- **`display_word(secret_word, guessed_letters)`**: Renders masked word (shows guessed letters, blanks for unknown)
- **`validate_input()`**: Loops until receiving valid single letter (alpha only)
- **`play_game()`**: Orchestrates game loop, tracks state, determines win/loss conditions
-  get_auto_guess(guessed_letters): im going to use this to guess the next letter based on the already guessed letter that it found

Notes:
the auto play not done yet i think i need more thinking time.