name_list = []

while True:
    name_list_set = {name.casefold() for name in name_list}
    enter_name = input("Enter a name: ")
    if enter_name.casefold() in name_list_set:
        print("Existing name!")
    else:
        print("New Name!")
        name_list.append(enter_name)