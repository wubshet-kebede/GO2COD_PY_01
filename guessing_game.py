import random

def number_guessing_game():
    """Generates a random number and lets the user guess it."""

    number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0  # Initialize the attempt counter

    print("Welcome to the Number Guessing Game!")
    print("I've chosen a number between 1 and 100. Can you guess it?")

    while True:
        try:
            guess = int(input("Enter your guess: "))  # Get user input and convert to integer
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue  # Continue to the next iteration of the loop

        attempts += 1  # Increment attempt counter

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            break  # Exit the loop if the guess is correct

if __name__ == "__main__":
    number_guessing_game()