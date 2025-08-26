input_value = None
min_max_list = []
print(f"Enter a bunch of numbers, we'll let you know which is the "
      f"highest and lowest.")
while input_value != "":
    input_value = input("Enter a number: ")
    if input_value != "":
        input_value = int(input_value)
        min_max_list.append(input_value)

if min_max_list:
    min_value = min(min_max_list)
    max_value = max(min_max_list)
    print(f"The lowest number you entered was {min_value}, and the highest "
      f"was {max_value}.")

print("You didnt enter any numbers.")
