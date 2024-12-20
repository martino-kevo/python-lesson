import sys
import threading
import time
import random


class ThreeNumberGuessingGame:

    def __init__(self):
        pass

    def play(self, player_money):

        if type(player_money) != int:
            print("\nEnter real money")
        elif player_money != 200:
            print("\nYou can only play with 200 naira at this moment")
        else:

            print("\n" + "3 numbers guessing game".upper().center(30))
            print("Win 50x of your money".title().center(30))
            print("\n******** Disclamer ********\nThis bet is extremely risky,\nthat's why the creator has\nlimited the playing fee to 200 naira")
            print("\nChoose from 1 - 10".title())

            first_input = input("\nEnter first number\n")
            second_input = input("\nEnter second number\n")
            third_input = input("\nEnter third number\n")

            if (not first_input.isdecimal() or int(first_input) > 10) or (not second_input.isdecimal() or int(second_input) > 10) or (not third_input.isdecimal() or int(third_input) > 10):
                print("\nEnter a whole number value or read the instructions carefully!")
                return self.play(200)
            else:
                def game_outcome(input1, input2, input3):

                    nonlocal player_money

                    first_number = random.choice(range(1, 11))
                    second_number = random.choice(range(1, 11))
                    third_number = random.choice(range(1, 11))

                    print()

                    def f_num():
                        time.sleep(1)
                        print(str(first_number))

                    def s_num():
                        time.sleep(1)
                        print(str(second_number).rjust(10))

                    def t_num():
                        time.sleep(1)
                        print(str(third_number).rjust(20))

                    thread1 = threading.Thread(target=f_num)
                    thread2 = threading.Thread(target=s_num)
                    thread3 = threading.Thread(target=t_num)

                    thread1.start()
                    thread2.start()
                    thread3.start()

                    thread1.join()
                    thread2.join()
                    thread3.join()

                    if input1 == first_number and input2 == second_number and input3 == third_number:
                        money_won = player_money * 50
                        print(f"\nCongratulations 🎉🎉🎉! You just won {
                              money_won} naira")
                    else:
                        print(f"\nWhoops! You just lost {
                              player_money} naira\nTry again 😁\n")

                game_outcome(first_input, second_input, third_input)

                while True:
                    return self.play(200)


three_number_guessing_game = ThreeNumberGuessingGame()

three_number_guessing_game.play(200)
