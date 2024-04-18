
def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if right[j] > left[i]:
            print(left[i])
            result.append(left[i])
            print('hi1')
            print(result)
            i += 1
        else:
            result.append(right[j])
            print('hi2')
            print(result)
            j += 1
    while i < len(left):
        result.append(left[i])
        print('hi3')
        print(result)
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1

    return result


def merge_sort(list):
    """
    sorts a list in ascending order
    Returns a sorted list
    Divide and conquer first finds the middle element and
    then recursively sorts the sublist until it reaches the
    end of the list
    """

    if len(list) <= 1:
        return list

    mid = len(list) // 2
    print(mid)
    print('mid')
    left = merge_sort(list[:mid])
    print("left")
    print(left)
    right = merge_sort(list[mid:])
    print("right")
    print(right)
    return merge(left, right)


number = [2, 4, 6, 5, 8, 1, 3, 9, 10, 7]
#number = [54, 62, 93, 17, 77, 31, 44, 55, 20]

result = merge_sort(number)
print(result)
