# Lab 4 Word Game - Development Journal & AI Interaction Log

**Purpose**: Document the iterative development of a Hangman-style console game using AI-assisted design and implementation.

---

## Phase 1: Core Game Logic & Design

**Date**: 03-11-2026  
**Prompt**: "Let's vibe code a Hangman-style console game. I need a main.py that picks a random word from a list, has 6 turns by default, and shows the word as _ _ S _ E. Track the guessed letters and turns left. Make it look clean in the terminal and add input validation so it doesn't crash on numbers or empty strings."

**AI Response**: Provided Socratic guidance asking about:
- Game state tracking (word, guesses, turns)
- Word display format
- Input validation rules
- Win/loss conditions
- Code organization (function breakdown)

**Outcome**: Established foundational architecture with four functions: `pick_word()`, `display_word()`, `validate_input()`, `play_game()`

---

## Phase 2: Feature Refinement & Variable Design

**Date**: 03-11-2026  
**Prompt**: "What variables should I have for every function?"

**AI Response**: Guided analysis of game state variables and their relationships:
- `secret_word` (str): Target word
- `guessed_letters` (list): Accumulating correct/incorrect guesses
- `turns_left` (int): Remaining attempts
- Design question about parameter passing philosophy

**Outcome**: Clarified variable scope and responsibilities across functions. Determined that `play_game()` manages core state while helper functions receive only necessary parameters.

---

## Phase 3: Input Validation & Bug Prevention

**Date**: 03-11-2026  
**Prompt**: "Summarize my 'architect brain' for this project into MY_NOTES.md. List the game states (init, loop, win/loss), the main variables we used, and the edge cases we guarded against (like double-guessing or non-alpha chars). Keep it professional but concise."

**AI Response**: Documented comprehensive edge-case handling:
- Empty input guard: `len(guess) != 1`
- Non-alphabetic input: `.isalpha()` validation
- Duplicate guess detection: `if guess in guessed_letters`
- Case normalization: `.lower()` on all input
- Conditional turn penalty: Only decrement on wrong guess

**Outcome**: Created MY_NOTES.md architecture summary. Validated that all major error cases are prevented before they crash the game.

---

## Summary: AI-Assisted Development Workflow

| Phase | Focus | AI Role |
|-------|-------|---------|
| 1 | Core Logic | Socratic guidance on system design |
| 2 | Architecture | Guided variable scope analysis |
| 3 | Robustness | Documented edge cases & validation |

**Total AI Interactions**: 3 prompts  
**Result**: Fully functional Hangman game with clean terminal UI, input validation, and clear separation of concerns
- **Date**: 03-09-2026 11:57
- **User**: default_user
- **Prompt**: "update the journal with the recent interactions"
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Performed mandatory reconciliation workflow, identified and logged missing interactions, updated JOURNAL.md with cumulative session history
- **Context and Reasons for Changes**: 
  - Implemented reconciliation protocol to capture all interactions since journal initialization
  - Identified two missing interactions: "yes do it" confirmation and current update request
  - Maintained reverse-chronological order (newest entries first)
  - All entries now include consistent timestamp, mode, and model metadata
- **My Observations**: 

---

### **Confirmation - Enable Journal & Socratic Mode**
- **Date**: 03-09-2026 11:50
- **User**: default_user
- **Prompt**: "yes do it"
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Confirmed activation request, proceeded with reading journal-logger.agent.md and retrieving system timestamp
- **Context and Reasons for Changes**: 
  - User confirmed intent to activate journal system and read instructions
  - Executed timestamp retrieval (03-09-2026 11:47) and git config lookup
  - Began initialization of JOURNAL.md with proper formatting
- **My Observations**: 

---

### **Journal Initialization & Activation**
- **Date**: 03-09-2026 11:47
- **User**: default_user
- **Prompt**: "read copilot-instructions.md and activate the journal"
- **CoPilot Mode**: Ask
- **CoPilot Model**: Claude Haiku 4.5
- **Changes Made**: Initialized JOURNAL.md tracking system, reviewed and activated copilot-instructions.md requirements
- **Context and Reasons for Changes**: 
  - Activated Socratic Mode (default ON) to guide learning through questions rather than direct code solutions
  - Established journal logger protocol per journal-logger.agent.md specifications
  - Configured reverse-chronological ordering (newest entries at top)
  - Set up mandatory reconciliation workflow to prevent duplicate entries
  - All future interactions will be logged following this template
- **My Observations**: 

