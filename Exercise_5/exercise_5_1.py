import random

no_rolls = int(input("Enter the number of dice to roll: "))
total = 0

for rolls in range(no_rolls):
    total += random.randint(1,6)

print(total)
