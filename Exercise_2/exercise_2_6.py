import random
first_of_3 = random.randint(0, 9)
second_of_3 = random.randint(0, 9)
third_of_3 = random.randint(0, 9)

print("3-digit code:")
print(int(str(first_of_3) + str(second_of_3) + str(third_of_3)))

first_of_4 = random.randint(1, 6)
second_of_4 = random.randint(1, 6)
third_of_4 = random.randint(1, 6)
forth_of_4 = random.randint(1, 6)
print()
print("4-digit code:")
print(int(str(first_of_4) + str(second_of_4) + str(third_of_4) + str(forth_of_4)))


# This other way leaves a space between the numbers, I'm not sure which  to submit
print("\n" + "=" * 50 + "\n")
print("3-digit code:")
print(first_of_3, second_of_3, third_of_3)
print()
print("4-digit code:")
print(first_of_4, second_of_4, third_of_4, forth_of_4)