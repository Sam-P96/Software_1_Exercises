import random

print("I have drawn a random integer between 1 and 10. What integer have i drawn?")
solution = random.randint(1, 10+1)

answer = 0
while answer != solution:
    answer = int(input("Enter Guess: "))
    if answer < solution:
        print("Please guess higher")
    elif answer > solution:
        print("Please guess lower")
    else:
        break

print("You guessed {}, that's correct!".format(solution))