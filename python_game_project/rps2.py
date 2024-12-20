import sys
import random
from enum import Enum


def rps(name):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():

        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        player_input = input(
            f"\n {name}, please enter...\n 1 for Rock \n 2 for Paper \n 3 for Scissors :\n\n")

        if player_input not in ['1', '2', '3']:
            print(f"{name}, please enter 1, 2 or 3")
            return play_rps()

        player_choice = int(player_input)

        computer_input = random.choice("123")

        computer_choice = int(computer_input)

        print(f"\n{name}, you chose {
              str(RPS(player_choice)).replace("RPS.", "").title()}."
              )
        print(f"Python chose {
              str(RPS(computer_choice)).replace("RPS.", "").title()}.\n"
              )

        def decide_winner(player_choice, computer_choice):

            nonlocal player_wins
            nonlocal python_wins

            if (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
                player_wins += 1
                with open("python_game_project/game_record.txt", "a") as file:
                    file.write("1".ljust(16) + "-->" +
                               "Won".rjust(16) + "\n")
                return f"You win {name}! 😎"
            elif player_choice == computer_choice:
                with open("python_game_project/game_record.txt", "a") as file:
                    file.write("-".ljust(16) + "-->" +
                               "Tie".rjust(16) + "\n")
                return "Tie game! 😲"
            else:
                python_wins += 1
                with open("python_game_project/game_record.txt", "a") as file:
                    file.write("0".ljust(16) + "-->" +
                               "Lost".rjust(16) + "\n")
                return f"Python wins {name}!\n Sorry 😝 \n"

        game_result = decide_winner(player_choice, computer_choice)

        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"Game count: {game_count}")
        print(f"{name} {player_wins} : {python_wins} Python")

        print(f"\n Play again {name} 🌝")

        while True:
            play_again = input("\n Y for yes  \n Q to Quit: \n\n")
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == "y":
            return play_rps()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!")
            if __name__ == "__main__":
                sys.exit(f"\nBye {name}! 👋 \nSee you again next time.\n")
            else:
                return

    return play_rps


# Making rps2 a module
if __name__ == "__main__":

    import os
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", default="PlayerOne",
        required=False, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)

    if os.path.exists("python_game_project/game_record.txt"):
        os.remove("python_game_project/game_record.txt")

    with open("python_game_project/game_record.txt", "a") as file:
        file.write("Game Record For ROCK PAPER SCISSORS\n\n")

    rock_paper_scissors()
