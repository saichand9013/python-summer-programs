#LEVEL2-T1
#Task: Guessing Game
#Write a Python program that generates a random number between 1 and 100. Theuser should then tryto guess the number.The program should provide hints such as"too high" or "too low" until the correctnumber is guessed.'''

import random

secret_number = random.randint(1, 100)# Generate a random number between 1 and 100

attempts = 0 #user has attempts # Initialize the number of attempts
def check_guess(guess, secret_number):
    if guess == secret_number:
        return "Correct"
    elif guess < secret_number:
        return "Too low"
    else:
        return "Too high"

print("Welcome to the Number Guessing Game!")# Play the game
while True:

    guess = int(input("Guess a number between 1 and 100: "))# Get the user's guess
    result = check_guess(guess, secret_number)# Check the user's guess
    print(result)#result


    attempts += 1 #Increment the number of attempts

# Check if the user has won
    if result == "Correct":
        print(f"Congratulations! You guessed the secret number {secret_number} in {attempts} attempts.")
        break
