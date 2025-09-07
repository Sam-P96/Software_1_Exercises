import random


def roll_x(sides: int) -> int:
    """
    Functions generates a number at random between 1 and `n` th number.
    :param sides: The `n` th number. The highest number the function can
    generate.
    :return: Returns an int, the random number generated.
    """
    result = random.randint(1, sides)
    return result



print("""This program will roll dice with the number of sides of your
choosing. It will stop when it rolls the highest number.""")
target = int(input("Please how many sides this dice have:"))

max_roll = 0

while max_roll!= target:
    max_roll = roll_x(target)
    print(max_roll)