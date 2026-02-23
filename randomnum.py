from random import randint
import time

print
'=' * 20
print
'The Up / Down Game'
print('Enter up or down !')
print('Get 10 in a row for a reward!')
print('=' * 20)
print("=    " + 'GAME START' + "    =")
print('=' * 20)
print('')

ans = ' '
score = 0

while True:
    n1 = randint(2, 13)
    n2 = randint(2, 13)
print("I have = %s" % (n1))

ans = raw_input("What do you choose: ")

if ans == 'up':
    print("Your number is : ")
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(". %s" % n2)
    time.sleep(1)
    if n1 > n2:
        print("Sorry you lost.")
        time.sleep(2)
        print("Final score = %s" % score)
        time.sleep(2)
        print("=" * 20)
        print("Try Again")
        print("=" * 20)
        score = 0

    elif n1 <= n2:
        score += 1
        if score > 1:
            print("That's %s in a row" % score)
        elif score == 1:
            print
            "Thats  1 point"
        elif score == 10:
            print
            "Congratz you got the reward!!!"

elif ans == 'down':
    print
    "Your number is : "
    time.sleep(0.5)
    print
    "."
    time.sleep(0.5)
    print
    ". %s" % n2
    time.sleep(1)
    if n1 < n2:
        print
        "Sorry you lost."
        time.sleep(2)
        print
        "Final score = %s" % score
        time.sleep(2)
        print
        "=" * 20
        print
        "Try Again"
        print
        "=" * 20
        score = 0

    elif n1 >= n2:
        score += 1
        if score > 1:
            print
            "That's %s in a row" % score
        elif score == 1:
            print
            "Thats  1 point"
        elif score == 10:
            print
            "Congratz. You got the reward"


    else:
        tryAgain = raw_input("enter up or down only")