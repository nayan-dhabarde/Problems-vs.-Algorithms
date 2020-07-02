

def quick_sort(input_list):
    sort(input_list, 0, len(input_list) - 1)


def sort(arr, start, end):
    if end <= start:
        return

    pivot_index = partial_sort(arr, start, end)
    sort(arr, start, pivot_index - 1)
    sort(arr, pivot_index + 1, end)


def partial_sort(arr, left, right):
    pivot_index = right
    pivot_value = arr[pivot_index]

    while pivot_index != left:
        if arr[left] < pivot_value:
            arr[pivot_index] = arr[left]
            arr[left] = arr[pivot_index - 1]
            arr[pivot_index - 1] = pivot_value
            pivot_index -= 1
        else:
            left += 1

    return pivot_index


def rearrange_digits(input_list):
    quick_sort(input_list)
    num1 = 0
    num2 = 0

    for i in range(len(input_list)):
        if i % 2 == 0:
            num1 *= 10
            num1 += input_list[i]
        else:
            num2 *= 10
            num2 += input_list[i]

    return [num1, num2]
    pass


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)    # returns Pass

test_case = [[1, 2, 3, 4, 5], [531, 42]]
test_function(test_case)    # returns Pass

test_case = [[1, 2, 3, 4, 5], [521, 43]]
test_function(test_case)    # returns Fail




