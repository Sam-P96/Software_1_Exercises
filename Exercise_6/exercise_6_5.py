def list_even(even_odd: list) -> list:
    """
    Takes in a list of integers, removes all even numbers, but keeps
    the list in the same order.
    :param even_odd: list of integers
    :return: list of integers with only odd numbers
    """
    odd_only = []
    for number in even_odd:
        if number % 2 != 0:
            odd_only.append(number)
    return odd_only



all_no = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
x = list_even(all_no)
print(x)