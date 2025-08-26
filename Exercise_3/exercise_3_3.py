sex = input("""Select your biological sex: 
A. Male 
B. Female
C. Intersex
Enter selection: """)

while True:
    if sex == "C".casefold():
        print("Sorry, we do not have enough data to gauge if your hemoglobin values are within normal range.")
        break
    elif sex == "A".casefold():
        hg_lvl = float(input("Please enter your hemoglobin level: "))
        if  134 <= hg_lvl <= 167:
            print("Your hemoglobin levels are within normal range")
            break
        elif hg_lvl > 167:
            print("Your hemoglobin levels are too high.")
            break
        else:
            print("Your hemoglobin levels are too low")
            break
    elif sex == "B".casefold():
        hg_lvl = float(input("Please enter your hemoglobin level: "))
        if  117 <= hg_lvl <= 155:
            print("Your hemoglobin levels are within normal range")
            break
        elif hg_lvl > 155:
            print("Your hemoglobin levels are too high.")
            break
        else:
            print("Your hemoglobin levels are too low.")
            break
    else:
        print("Error. Please try again.")
        sex = "not selected"
        break