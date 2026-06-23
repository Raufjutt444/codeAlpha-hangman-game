import random

def play_hangman():
    # 1. Setup: Small list of 5 predefined words
    words = ["python", "variable", "function", "integer", "string"]
    
    # Select a random word from the list
    secret_word = random.choice(words)
    
    # Game state variables
    guessed_letters = []
    incorrect_guesses_left = 6
    
    print("Welcome to Text-Based Hangman!")
    
    # 2. Main Game Loop (while loop)
    while incorrect_guesses_left > 0:
        
        # Construct the word display (e.g., p _ t h _ n)
        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
                
        print(f"\nWord: {display_word.strip()}")
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
        
        # Check for a win
        if "_" not in display_word:
            print(f"\nCongratulations! You guessed the word: '{secret_word}'")
            return  # Exit the game
            
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Input validation (if-else)
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try a different one!")
            continue
            
        # Add the valid guess to our list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct or incorrect
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses_left -= 1
            
    # 3. Game Over State
    print(f"\nGame Over! You have run out of guesses.")
    print(f"The secret word was: '{secret_word}'")

# Run the game
if __name__ == "__main__":
    play_hangman()