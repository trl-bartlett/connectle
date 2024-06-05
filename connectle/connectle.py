import os

# ASCII art
ascii_art = """    
 .o88b.  .d88b.  d8b   db d8b   db d88888b  .o88b. d888888b db      d88888b
d8P  Y8 .8P  Y8. 888o  88 888o  88 88'     d8P  Y8 `~~88~~' 88      88'    
8P      88    88 88V8o 88 88V8o 88 88ooooo 8P         88    88      88ooooo
8b      88    88 88 V8o88 88 V8o88 88~~~~~ 8b         88    88      88~~~~~
Y8b  d8 `8b  d8' 88  V888 88  V888 88.     Y8b  d8    88    88booo. 88.    
 `Y88P'  `Y88P'  VP   V8P VP   V8P Y88888P  `Y88P'    YP    Y88888P Y88888P
"""

# Dictionary of subjects and words
connection_dictionary = {
    "still life painting subjects": {"fruit", "tablecloth", "skull", "glass"},
    "sonic the hedgehog characters": {"knuckles", "blaze", "espio", "rosey"},
    "film equipment": {"dolly", "lense", "boom", "lights"},
    "authors last names": {"bolano", "eco", "atwood", "spencer"}
}

# Function to display the current state of the game
def display_state(hidden_words, attempts_left, used_letters, completed_sets):
    print("words: ", "  ".join(hidden_words))
    print(f"attempts left: {attempts_left}")
    print(f"used letters: {', '.join(sorted(used_letters))}")
    print("\ncompleted sets:")
    for completed_set in completed_sets:
        print(f"- {completed_set}\n")

# List to keep track of completed sets
completed_sets = []

# Clear the screen once at the start of the game
os.system('cls')  # Use 'cls' for Windows

# Iterate over each set of words in the dictionary
for key, word_set in connection_dictionary.items():
    word_list = list(word_set)
    hidden_words = ["_" * len(word) for word in word_list]

    game_end = False
    attempts_left = 10
    used_letters = set()

    while not game_end and attempts_left > 0:
        
        print(ascii_art)
        
        display_state(hidden_words, attempts_left, used_letters, completed_sets)

        # Prompt user for a letter
        user_guess = input("\nenter a letter: ").lower()

        # If user_guess is not a single letter, prompt again
        if len(user_guess) != 1 or not user_guess.isalpha():
            print("please enter a single letter.")
            continue

        # Add the guessed letter to the used letters set
        used_letters.add(user_guess)

        # Check if the guessed letter is in any of the words
        correct_guess = False
        for i, word in enumerate(word_list):
            if user_guess in word:
                correct_guess = True
                # Replace the underscores with the correctly guessed letter
                hidden_words[i] = "".join(
                    user_guess if word[j] == user_guess else hidden_words[i][j]
                    for j in range(len(word))
                )

        if not correct_guess:
            attempts_left -= 1

        # Check if the game is won
        if "_" not in "".join(hidden_words):
            game_end = True

    # Display final state for the current set of words
    display_state(hidden_words, attempts_left, used_letters, completed_sets)
    if game_end:
        print(f"congratulations! you've guessed all the words for '{key}'!")
        completed_sets.append(key)
    else:
        print(f"out of attempts! the words for '{key}' were: {', '.join(word_list)}")
        break  # Exit the loop if out of attempts

# Display final state after completing all sets or running out of attempts
display_state(hidden_words, attempts_left, used_letters, completed_sets)
if game_end and len(completed_sets) == len(connection_dictionary):
    print("congratulations! uou've guessed all the words in all sets!")
else:
    print("game over. better luck next time.")
