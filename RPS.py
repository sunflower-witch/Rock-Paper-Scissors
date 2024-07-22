import random
import time


def check(the_player, comp_choice, user_choice):
    choices = {player: user_choice, "Computer": comp_choice}
    print(f"{RED_COLOR}{player}{RESET} chose {user_choice}, {YELLOW}Computer{RESET} chose {comp_choice}")

    if user_choice == comp_choice:
        return "draw"
    elif user_choice == "rock" and comp_choice == "scissors":
        return the_player
    elif user_choice == "paper" and comp_choice == "rock":
        return the_player
    elif user_choice == "scissors" and comp_choice == "paper":
        return the_player
    else:
        return "Computer"


def choice(player_input):
    if player_input == 1:
        return "rock"
    elif player_input == 2:
        return "paper"
    else:
        return "scissors"


def play(player_name):
    play_again = True
    while play_again:
        try:
            user_pick = int(input(
                f"{SECOND_COLOR}Whats your pick? \n"
                f"1 = rock 🎼, 2 = paper 💸 or 3 = scissors ✂️ {RESET} {YELLOW}(p.s. Computer can't read){RESET}\n"))
        except ValueError:
            print(f"Please pick: 1 for rock, 2 for paper or 3 for scissors")
            continue
        user = choice(user_pick)
        print(f"You picked: {user}")
        print(f"{FIRST_COLOR}Now Computer will take it's time picking...{RESET}")
        time.sleep(1)
        computer_pick = random.randint(1, 3)
        computer = choice(computer_pick)
        winner = check(player_name, computer, user)
        time.sleep(1)
        if winner != "draw":
            print(f"{WINNER_COLOR}{winner} is the winner!{RESET}")
        else:
            print(f"{FIRST_COLOR}It's a draw!{RESET}")
        print(f"{WINNER_COLOR}Do you want to play again?{RESET} {FIRST_COLOR}Y{RESET}/{RED_COLOR}N{RESET}")
        pick = input().strip().upper()
        if pick != "Y":
            play_again = False


def rgb_escape_code(r, g, b):
    return f"\033[38;2;{r};{g};{b}m"


# Colors for text
WINNER_COLOR = rgb_escape_code(171, 157, 255)  # lilac for winner
RED_COLOR = rgb_escape_code(255, 157, 169)  # red
FIRST_COLOR = rgb_escape_code(157, 255, 179)  # green
SECOND_COLOR = rgb_escape_code(157, 226, 255)  # teal
YELLOW = rgb_escape_code(255, 222, 106)  # yellow

RESET = "\033[0m"  # Reset color

print(f"{SECOND_COLOR}Welcome to Rock 🎼 Paper💸 Scissors ✂️{RESET}")
player = input("What's your name? ")
print(f"That's great, {player}! My name is Computer. Let's play!")
play(player)
print(f"{WINNER_COLOR}Thanks for playing!💜{RESET}")
