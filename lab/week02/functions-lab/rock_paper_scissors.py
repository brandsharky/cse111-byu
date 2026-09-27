import random



def computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def user_choice():
    users_choice = str(input("Rock, paper, or scissors: "))
    return users_choice


def determine_winner():
    user = user_choice()
    computer = computer_choice()

    print()
    print(f"User chose: {user}")
    print(f"Computer chose: {computer}")

    if user == "rock":
        if computer == "paper":
            return "You lose!"
        elif computer == "scissors":
            return "You win!"
        else:
            return "It's a tie!"
    elif user == "paper":
        if computer == "scissors":
            return "You lose!"
        elif computer == "rock":
            return "You win!"
        else:
            return "It's a tie!"
    else:
        if computer == "rock":
            return "You lose!"
        elif computer == "paper":
            return "You win!"
        else:
            return "It's a tie!"





if __name__ == "__main__":
    print(determine_winner())