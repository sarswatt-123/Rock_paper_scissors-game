import random

# Initialize scores
user_score = 0
computer_score = 0

while True:
    # Prompt the user to choose rock, paper, or scissors
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    # Check if the user's choice is valid
    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Generate a random choice for the computer
    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    # Display the choices
    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    # Display the current scores
    print(f"Your score: {user_score}")
    print(f"Computer score: {computer_score}")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print("Thanks for playing!")
