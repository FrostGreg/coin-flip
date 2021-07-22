import random
import sys
import time

print("========Welcome to the Coin Flip Sim========")

while 1:
    a = random.randrange(0, 2)

    s = '.'
    sys.stdout.write("Flipping")
    for i in range(5):
        sys.stdout.write(s)
        time.sleep(0.5)

    if a == 1:
        print("\nHeads!")
        time.sleep(1)

    else:
        print("\nTails!")
        time.sleep(1)

    rep = input("Would you like to flip again?:   ").lower()
    if rep != "yes":
        break

print("Thank you for using this coin flip sim :)")
