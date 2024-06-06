#LEVEL2-T2
#Task: Number Guesser
#Create a number guessing game where the program generates a random number between a specified range, and the user tries to guess it. Provide feedback to the user if their guess is too high or too low.'''

import random
min_range = int(input("Enter the minimum range: "))#min
max_range = int(input("Enter the maximum range: "))#max
# Generate a random number between the specified range
secret_number = random.randint(min_range, max_range)
attempts = 0
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"
# Play the game
print(f"Welcome to the Number Guessing Game! The range is between {min_range} and {max_range}.")
while True:
    guess = int(input("Guess a number: "))
    result = check_guess(guess, secret_number)
    # Print the result
    print(result)
    # Increment the number of attempts
    attempts += 1
    # Check if the user has won
    if result == "Correct":
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break
