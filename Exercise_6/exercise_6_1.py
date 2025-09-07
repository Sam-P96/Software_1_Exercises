import random


def roll_6() -> int:
    """
    Function generates a random int between 1 and 6.
    :return: Returns an int, the random number generated.
    """
    result = random.randint(1, 6)
    return result



input("Please press enter to start rolling dice until you get a 6.")

please_6 = 0

while please_6 != 6:
    please_6 = roll_6()
    print(please_6)