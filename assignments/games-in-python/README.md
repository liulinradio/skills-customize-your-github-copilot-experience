
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a word-guessing game in Python to practice strings, loops, conditionals, random selection, and user input.

## 📝 Tasks

### 🛠️ Choose a Word and Track Progress

#### Description
Complete the game setup so it randomly chooses a word and displays which letters the player has guessed correctly.

#### Requirements
Completed program should:

- Randomly select a secret word from the provided `words` list
- Track guessed letters and the number of incorrect guesses
- Display each letter in the secret word, showing unguessed letters as underscores


### 🛠️ Run the Guessing Game

#### Description
Implement the game loop so the player can guess letters until they reveal the word or run out of attempts.

#### Requirements
Completed program should:

- Prompt the player for one letter on each turn
- Reveal correctly guessed letters and count incorrect guesses toward the attempt limit
- End the game when the player guesses the word or reaches the maximum incorrect guesses
- Display a clear win or loss message and reveal the secret word if the player loses
