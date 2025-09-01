print("""Enter a bunch of numbers one at a time, I'll tell you which
        ones were the 5 highest numbers you entered. Press 0 to quit.""")
no_input = ""
no_list = []
while no_input != 0:
    no_input = int(input("Enter a number: "))
    no_list.append(no_input)

no_list.sort(reverse = True)
print(no_list[0:5])