air_dict = {"EFHK": "Helsinki-Vantaa Airport",
            "WSSS": "Changi Airport",
}

while True:
    print("""What would you like to do?
    1. Fetch information on existing airport
    2. Enter a new airport
    0. Exit program""")
    select = input("Enter choice: ")
    if select == "1":
        icao_1 = input("Please enter the ICAO code of the desired airport: ")
        if icao_1 in air_dict:
            print(f"ICAO: \"{icao_1}\" is designated to {air_dict[icao_1]}.")
            print("=" * 80)
        else:
            print(f"\"{icao_1}\" could not be located in our systems.")
            print("Please keep in mind ICAO codes are case sensitive.")
            print("="*80)
    elif select == "2":
        print("""You have chosen to enter a new airport. You can cancel by entering \"0\".""")
        name_2 = input("Please enter the name of the new airport: ")
        if name_2 == "0":
            print("=" * 80)
            continue
        else:
            icao_2 = input(f"Please the ICAO for {name_2}: ")
            if icao_2 in air_dict:
                over_w = input(f"""\"{icao_2}\" already exists in our system. Would you like to reassign it?
1. Yes
2. No
Enter choice: """)
                if over_w == "1" or over_w.casefold() == "yes":
                    print(f"{name_2} has been assigned as \"{icao_2}\"")
                    air_dict[icao_2] = name_2
                    print("=" * 80)
                elif over_w == "2" or over_w.casefold() == "no":
                    print(f"{icao_2} will not be overwritten.")
                    print("=" * 80)
                else:
                    print("You did not choose a valid option.")
                    print("=" * 80)
            elif icao_2 not in air_dict:
                print(f"{name_2} has been assigned as \"{icao_2}\"")
                air_dict[icao_2] = name_2
                print("=" * 80)
    elif select == "0":
        print("-Program Ended-")
        break
    else:
        print("Please enter a valid option.")