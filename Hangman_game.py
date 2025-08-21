import random

def hangman():
    """
    A simple text-based Hangman game.
    """
    words = ["python", "hangman", "computer", "programming", "developer"]
    secret_word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman! Let's get started.")
    print("_ " * len(secret_word))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print(f"Good guess! The letter '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, the letter '{guess}' is not in the word.")
            print(f"You have {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        display_word = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        if "_" not in display_word:
            print(f"Congratulations! You guessed the word: '{secret_word}'")
            break

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Game over! You ran out of guesses. The word was '{secret_word}'.")

if __name__ == "__main__":
    hangman()