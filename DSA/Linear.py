def linear_search(list, target):
    """
    Returns the index of the target if it exists and is in the list, else returns -1
    :param list:
    :param target:
    :return:
    """
    for i in range(0, len(list)):
        print(i)
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("The index is:" + str(index))
    else:
        print("The index isn't found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 8)

verify(result)
