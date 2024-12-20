import threading
import time


# def walk_dog(firstname, lastname):
#     time.sleep(8)
#     print(f'You finish walking {firstname} {lastname}')


# def take_out_trash():
#     time.sleep(2)
#     print('You take out the trash')


# def get_mail():
#     time.sleep(4)
#     print('You get the mail')


# print()

# chore1 = threading.Thread(target=walk_dog, args=('Scooby', 'Doo'))
# chore1.start()

# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()

# chore3 = threading.Thread(target=get_mail)
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("All chores are complete")

count = 0

num = input('\nWhat number do you want the values to\nprint to?\n\n')


def increment_count(c):

    try:
        for i in range(c):

            time.sleep(1)

            global count
            count += 1
            print(count)
    except TypeError:
        print('Strings cannot be interpreted by python as integers')


try:
    num = int(num)
except ValueError:
    print('You cannot cast an integer to a string')

print()
thread1 = threading.Thread(target=increment_count,
                           args=(num,), name="Incrementing count Thread")

thread1.start()


input("Press enter to execute the remaining code in the main thread\n")

print(f"\nThe value of count is {count}")

num = bin(25)

print(num)
