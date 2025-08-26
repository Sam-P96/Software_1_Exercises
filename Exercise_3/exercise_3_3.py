while True:
    sex = input("""Select your biological sex: 
A. Male 
B. Female
Enter selection: """)
    if sex == "A".casefold() or sex == "MALE".casefold() or sex == "M".casefold():
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
    elif sex == "B".casefold() or sex == "FEMALE".casefold() or sex == "F".casefold():
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
