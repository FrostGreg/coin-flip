import random
import sys
import time
x = 0

print("========Welcome to the Coin Flip Sim========")

while x == 0:
    a = random.randrange(0,2)

    s = '.'
    sys.stdout.write("Flipping")
    for i in range(5):
        sys.stdout.write(s)
        sys.stdout.flush()
        time.sleep(0.5)

    if a == 1:
        print("\nHeads!")
        time.sleep(1)
        
    else:
        print("\nTails!")
        time.sleep(1)

    rep = input("Would you like to flip again?:   ")
    if rep == "Yes" or rep == "yes":
        x = 0
        
    elif rep == "No" or rep == "no":
        x = 1
        print("Thank you for using this coin flip sim :)")
        time.sleep(0.5)


end = input("Press any key to exit...")
