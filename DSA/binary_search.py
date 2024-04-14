def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last) // 2  # // flow division rounds up to the nearest whole number
        print(mid)
        print("yes0")

        if list[mid] == target:
            print(mid)
            print("yes1")
            return mid

        elif list[mid] < target:
            first = mid + 1
            print(first)
            print("yes2")

        elif list[mid] > target:
            last = mid - 1
            print(last)
            print("yes3")

    return None


def verify(index):
    if index is not None:
        print("The index is:" + str(index))
    else:
        print("The index isn't found")


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = binary_search(numbers, 3)
verify(result)
