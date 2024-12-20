import sys
import random


def guess_number(name):

    game_count = 0
    player_wins = 0

    def guess_num_func():

        nonlocal game_count, player_wins

        player_input = input(
            f"\n{name}, guess which number I'm thinking of... 1, 2, or 3.\n\n")

        if player_input not in ['1', '2', '3']:
            print(f"{name}, please enter 1, 2, or 3")
            return guess_num_func()
        else:
            player_choice = int(player_input)

            numbers = random.choice("123")
            computer_number = int(numbers)

            if player_choice == computer_number:
                game_count += 1
                player_wins += 1
                with open("python_game_project/game_record.txt", "a") as file:
                    file.write("1".ljust(14) + "-->" +
                               "Won".rjust(14) + "\n")
                print(f"\n{name}, you chose {
                      player_choice}.\nI was thinking about the number {computer_number}.")
                print(f"\n{name}, you win!")
            else:
                game_count += 1
                with open("python_game_project/game_record.txt", "a") as file:
                    file.write("0".ljust(14) + "-->" +
                               "Lost".rjust(14) + "\n")
                print(f"\n{name}, you chose {
                      player_choice}.\nI was thinking about the number {computer_number}.")
                print(f"\nSorry, {name}. Better luck next time. 😢")

            print(f"\nGame count: {game_count}")
            print(f"{name}'s wins: {player_wins}")

            percentage = (player_wins / game_count) * 100

            print(f"Your winning percentage: {percentage:.2f}%")

            print(f"\nPlay again, {name}")

            while True:
                play_again = input("\n Y for yes  \n Q to Quit\n\n")
                if play_again.lower() not in ['y', 'q']:
                    continue
                else:
                    break

            if play_again.lower() == "y":
                return guess_num_func()
            else:
                print(f"\n🎉🎉🎉🎉🎉\nThank you for playing.")
                if __name__ == "__main__":
                    sys.exit(f"\nBye {name}! 👋\n")
                else:
                    return

    return guess_num_func


if __name__ == "__main__":

    import os
    import argparse

    parser = argparse.ArgumentParser(
        description="This is number guessing game where you guess the number the computer is thinking."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=False, default="PlayerOne",
        help="The name of the person that is playing the games"
    )

    args = parser.parse_args()

    guess_my_number = guess_number(args.name)

    if os.path.exists("python_game_project/game_record.txt"):
        os.remove("python_game_project/game_record.txt")

    with open("python_game_project/game_record.txt", "a") as file:
        file.write("Game Record For GUESS MY NUMBER\n\n")

    guess_my_number()
