def l_g(gallons: float) -> float:
    """
    Converts gallons to litres.
    :param gallons: Volume of liquid in gallons.
    :return: Equivalent volume in litres.
    """
    litres = gallons * 3.7854
    return litres

g = float(input("Enter gallons to be converted to litres: "))
l = round(l_g(g), 3)
print(f"{l} litres")