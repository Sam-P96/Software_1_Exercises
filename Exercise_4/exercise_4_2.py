inch_cm = 1
while inch_cm > 0:
    print("Enter inches you want to convert to cm, you may enter a negative number to end the program.")
    inch_cm = float(input("Enter Inches: "))
    result = inch_cm * 2.54
    print(f"{inch_cm} inches converted, is {result}cm.")
    print("=" * 95 + "\n")

print("Program Ended")
