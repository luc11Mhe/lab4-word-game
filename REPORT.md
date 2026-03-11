# Lab 4: Hangman Word Game - Project Report

## Overview
This report confirms successful completion of a Hangman-style console game, developed iteratively with AI assistance. The application is a fully functional Python console application that can be executed via:

```bash
python ./main.py
```

---

## Functional Requirements - Verification

### ✅ Requirement 1: Random Word Selection
**Status**: MET  
**Implementation**: `pick_word()` function uses `random.choice()` to select from a curated word list (pizza, burger, sushi, waffle, fish, steak). Each game session selects a new random word from this pool.

### ✅ Requirement 2: Masked Word Display
**Status**: MET  
**Implementation**: `display_word(secret_word, guessed_letters)` renders the target word with revealed letters and blanks. Example: If word is "SUSHI" and player guessed "S", output is `S _ _ H I `.

### ✅ Requirement 3: Win Condition Detection
**Status**: MET  
**Implementation**: `all(letter in guessed_letters for letter in secret_word)` checks if every letter in the word has been guessed. When true, displays "You won!" message.

### ✅ Requirement 4: Loss Condition Detection
**Status**: MET  
**Implementation**: Game loop exits when `turns_left` reaches 0, triggering loss message: "You lost! The word was: [word]". Default turns set to 6.

### ✅ Additional Feature: Input Validation
**Status**: IMPLEMENTED  
Robust validation prevents common crashes:
- Rejects empty input (`len(guess) != 1`)
- Rejects non-alphabetic characters (`.isalpha()`)
- Detects and prevents duplicate guesses
- Normalizes input to lowercase (`.lower()`)

---

## Testing Strategy: unittest

We selected **unittest** as the testing framework for validation artifacts because it is Python's built-in standard library testing module, requiring no external dependencies, and provides a structured class-based approach that naturally mirrors the game's functional decomposition (`TestWordSelection`, `TestWordDisplay`, `TestInputValidation`, etc.).

---

## Architecture Summary

| Component | Purpose |
|-----------|---------|
| `pick_word()` | Selects random word |
| `display_word()` | Renders masked word state |
| `validate_input()` | Ensures valid single-letter input |
| `play_game()` | Orchestrates game loop & state |

**Primary State Variables**: `secret_word`, `guessed_letters`, `turns_left`  
**Game Loop Cycle**: Display → Prompt → Validate → Evaluate → Check Win/Loss

---

## Execution Summary

✅ All four functional requirements met  
✅ Console UI clean and user-friendly  
✅ Input validation prevents runtime errors  
✅ Clear win/loss messaging  
✅ Code organized into focused, testable functions  

**Status**: Ready for submission