while True:
    print("""Please select a cabin class from our available choices: 
        LUX: upper-deck cabin with a balcony.
        A: above the car deck, equipped with a window.
        B: windowless cabin above the car deck.
        C: windowless cabin below the car deck. """)
    choice = input("Selecting Cabin: ")
    if choice == "LUX".casefold():
        print("You selected LUX: upper-deck cabin with a balcony.")
        break
    elif choice == "A".casefold():
        print("You selected cabin A: above the car deck, equipped with a window.")
        break
    elif choice == "B".casefold():
        print("You selected cabin B: windowless cabin above the car deck.")
        break
    elif choice == "C".casefold():
        print("You selected cabin C: windowless cabin below the car deck")
        break
    else:
        print("Invalid cabin class selected.")
        print()
        print("=" * 80)
        print()