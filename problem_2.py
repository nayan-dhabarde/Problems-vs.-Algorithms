def rotated_array_search(input_list, number):

    if len(input_list) == 0:
        return -1

    if number is None or input_list is None:
        return -1

    pivot = find_pivot(input_list, 0, len(input_list) - 1)

    if pivot == -1:
        return rotated_binary_search(input_list, number, 0, len(input_list) - 1)

    if input_list[pivot] == number:
        return pivot

    if input_list[0] <= number:
        return rotated_binary_search(input_list, number, 0, pivot)

    return rotated_binary_search(input_list, number, pivot + 1, len(input_list) - 1)


def find_pivot(arr, start, end):

    if start >= end:
        return -1

    if start == end:
        return start

    mid = (start + end) // 2

    if arr[mid] > arr[mid + 1]:
        return mid

    if arr[mid] < arr[mid - 1]:
        return mid - 1

    if arr[mid] < arr[start] and arr[mid] < arr[end]:
        return find_pivot(arr, start, mid)

    return find_pivot(arr, mid + 1, end)


def rotated_binary_search(input_list, number, start, end):

    mid = (start + end) // 2

    mid_element = input_list[mid]

    if end > start:
        if mid_element == number:
            return mid
        elif number > mid_element:
            return rotated_binary_search(input_list, number, mid + 1, end)
        else:
            return rotated_binary_search(input_list, number, start, mid)
    else:
        return -1


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])    # prints Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])    # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8])           # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10])          # prints Pass
test_function([[6, 7, 8, 1, 2, 3, 4], None])          # prints Pass
test_function([[0], 1])          # prints Pass
test_function([[], 1])          # prints Pass
