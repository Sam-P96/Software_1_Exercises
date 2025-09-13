from math import pi

def spr(diameter: float, p_price: float) -> float:
    """
    Takes in the diameter and price of a pizza, and calculates the unit price
    :param diameter: diameter of the pizza
    :param p_price: price of the pizza
    :return: unit value of the pizza
    """
    sm = pi * (diameter ** 2)
    sp_ratio = sm / p_price
    return sp_ratio

print("""I will tell you whether the Pickled Pear & Herring or the 
Oysters & Ginger Lovers is better value for your money.""")

# Pickled Pear & Herring Pizza
dia = float(input("What is the diameter of the Pickled Pear & Herring Pizza?\n"))
price = float(input("What is the price of the Pickled Pear & Herring Pizza?\n"))

# Oysters & Ginger Lovers Pizza
dia_2 = float(input("What is the diameter of the Oysters & Ginger Lovers Pizza?\n"))
price_2 = float(input("What is the Price of the Oysters & Ginger Lovers Pizza?\n"))

if spr(dia, price) > spr(dia_2, price_2):
    print("The Pickled Pear & Herring Pizza is better value for your money.")
elif spr(dia_2, price_2) > spr(dia, price):
    print("The Oyster & Ginger Lovers Pizza is better value for your money.")
else:
    print("They are of equal value for your money.")


