def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    low = 0
    mid = 0
    high = len(input_list) - 1

    while mid <= high:
        if input_list[mid] == 0:
            input_list[mid], input_list[low] = input_list[low], input_list[mid]
            mid += 1
            low += 1

        elif input_list[mid] == 1:
            mid += 1

        elif input_list[mid] == 2:
            input_list[mid], input_list[high] = input_list[high], input_list[mid]
            high -= 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])                                                # returns Pass
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])   # returns Pass
test_function([2, 0, 2, 0, 0, 0, 2, 1, 0, 2, 0, 1])                                             # returns Pass
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])                        # returns Pass
