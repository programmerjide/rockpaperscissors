# #Rock-Paper-Scissors

#import necessary modules
import random

def main():
    # Create a list to store all possible options:
    # "R" for "rock",
    # "P" for "paper",
    # "S" for "scissors".
    options = ["R", "P", "S"]

    # When the program is run, ask the user to pick an option between "R", "P" or "S"
    user_input = input("Pick one: 'R' - Rock, 'P' - Paper, 'S' - Scissors: ")
    # If user input is invalid (not amongst our options), print an error, and ask for their input again (should be a loop)
    if user_input not in options:
        print("Invalid input")
        main()
    # Use the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
    cpu_choice = random.choice(options)
    # Print both player's moves in the format: `Player (Rock) : CPU (Paper)`
    print("Player: " + user_input + " CPU: " + cpu_choice)
    # Check both player's moves:
    # If there is a winner, print the winner, and the program ends.
    if user_input == cpu_choice:
        print("Tie")
        main()
    elif user_input == "R" and cpu_choice == "S":
        print("Player wins")
    elif user_input == "P" and cpu_choice == "R":
        print("Player wins")
    elif user_input == "S" and cpu_choice == "P":
        print("Player wins")
    else:
        print("CPU wins")

main()