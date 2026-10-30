import random

def get_choices():
    player_choice = input("Enter a choice (rock, paper, scissor): ").lower()

    options = ["rock", "paper", "scissor"]
    computer_choice = random.choice(options)

    choices = {
        "player": player_choice,
        "computer": computer_choice
    }

    return choices


def check_win(player, computer):
    print("\nYou chose:", player)
    print("Computer chose:", computer)

    if player == computer:
        return "It is a tie!"

    elif player == "rock":
        if computer == "scissor":
            return "Rock smashes Scissor! You Win!"
        else:
            return "Paper covers Rock! You Lose!"

    elif player == "paper":
        if computer == "rock":
            return "Paper covers Rock! You Win!"
        else:
            return "Scissor cuts Paper! You Lose!"

    elif player == "scissor":
        if computer == "paper":
            return "Scissor cuts Paper! You Win!"
        else:
            return "Rock smashes Scissor! You Lose!"

    else:
        return "Invalid choice! Please enter rock, paper, or scissor."


# Main Program
choices = get_choices()

result = check_win(
    choices["player"],
    choices["computer"]
)

print(result)