import random
from enum import Enum


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    play_again = True

    while play_again:

        player_input = input(
            "\n Enter...\n 1 for Rock \n 2 for Paper \n 3 for Scissors :\n\n")

        if player_input not in ['1', '2', '3']:
            print("You must enter 1, 2 or 3")
            continue

        player_choice = int(player_input)

        computer_input = random.choice("123")

        computer_choice = int(computer_input)

        print("\nYou chose " + str(RPS(player_choice)).replace("RPS.", "") + ".")
        print("Python chose " + str(RPS(computer_choice)
                                    ).replace("RPS.", "") + ". \n")

        if (player_choice == 1 and computer_choice == 3) or (player_choice == 2 and computer_choice == 1) or (player_choice == 3 and computer_choice == 2):
            print("You win bruh! 😎")
        elif player_choice == computer_choice:
            print("Tie game! 😲")
        else:
            print("Python wins! 😝 \n")

        print("\nPlay again")

        while True:
            play_again = input("\n Y for yes  \n Q to Quit: \n\n")
            if play_again.lower() not in ['y', 'q']:
                continue
            else:
                break

        if play_again.lower() == "y":
            continue
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!")
            print("Bye! 👋")
            play_again = False


play_rps()
