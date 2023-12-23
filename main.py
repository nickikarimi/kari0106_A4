import random

def choose_word():
    words = ["python", "hangman", "programming", "computer", "code", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_word()
    attempts = 0

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while attempts < max_attempts:
        guess = input("Guess a letter: ").lower()

        #check if the input is a single letter
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        #check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        #check if the guessed letter is in the word
        if guess not in word_to_guess:
            attempts += 1
            print(f"Wrong guess! {max_attempts - attempts} attempts left.")
        else:
            print("Correct guess!")

        current_display = display_word(word_to_guess, guessed_letters)
        print(current_display)

        #check if the player has guessed the entire word
        if "_" not in current_display:
            print("Congratulations! You've guessed the word!")
            break

    if "_" in current_display:
        print(f"Sorry, you're out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()

