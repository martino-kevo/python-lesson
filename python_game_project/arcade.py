from rps2 import rps
from guess_number import guess_number
import sys


def arcade(name):

    welcome_back = False

    while True:

        if welcome_back == True:
            print(f"\n{name}, welcome back to the Arcade! 🤖")

        player_choice = input(
            "\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press \"x\" to exit the Arcade\n\n")

        if player_choice not in ['1', '2', 'x']:
            print(f"{name}, please enter 1, 2 or x")
            return arcade(name)

        welcome_back = True

        if player_choice == '1':
            rock_paper_scissors = rps(name)
            rock_paper_scissors()
        elif player_choice == '2':
            guess_my_number = guess_number(name)
            guess_my_number()
        else:
            print("\nSee you next time")
            sys.exit(f"\nBye {name}! 👋")


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description="Arcade station - Have the most amazing gaming experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name", required=False, default="PlayerOne",
        help="The name of the person that is playing the games"
    )

    args = parser.parse_args()

    print(f"\n{args.name}, welcome to the Arcade! 🤖")

    arcade(args.name)
