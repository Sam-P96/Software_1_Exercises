def sum_all(number_list: list) -> int:
    """
    Takes in a list of integers and returns the sum of all the integers
    :param number_list: list of integers
    :return: sum of all the integers from the list given
    """
    total_x = 0
    for i in number_list:
        total_x += i

    return total_x



print("""This function will add all the numbers you entered up, and give
you the sum of all those numbers. You can enter 0 when you are done 
adding numbers.""")

list_1 = []
adder = 1
while adder != 0:
    adder = int(input("Enter a number:"))
    list_1.append(adder)

print(sum_all(list_1))