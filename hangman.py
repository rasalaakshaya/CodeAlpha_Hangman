import random

words = ["python", "java", "coding", "computer", "program"]

secret_word = random.choice(words)

display_word = ["_"] * len(secret_word)

wrong_guesses = 0
max_wrong_guesses = 6

print("==============================")
print("       HANGMAN GAME")
print("==============================")
print("You have 6 chances to guess the word.")

while wrong_guesses < max_wrong_guesses and "_" in display_word:

    print("\nWord:", " ".join(display_word))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in secret_word:
        print("Correct guess!")

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess

    else:
        wrong_guesses += 1

        print("Wrong guess!")
        print("Remaining chances:", max_wrong_guesses - wrong_guesses)

if "_" not in display_word:
    print("\n==============================")
    print("Congratulations! You won!")
    print("The word was:", secret_word)
    print("==============================")

else:
    print("\n==============================")
    print("Game Over!")
    print("The word was:", secret_word)
    print("==============================")