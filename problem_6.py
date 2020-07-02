def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if ints is None:
        return None

    if len(ints) == 0:
        return None

    min = ints[0]
    max = ints[0]

    for i in range(1, len(ints)):
        if ints[i] < min:
            min = ints[i]
        if ints[i] > max:
            max = ints[i]

    return min, max

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")    # returns Pass
random.shuffle(l)

print ("Pass" if ((0, 10) == get_min_max(l)) else "Fail")   # returns Fail
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")   # returns Pass

## Edge cases

print (get_min_max([]))   # returns None

print(get_min_max([0, 1]))   # returns 0, 1

print(get_min_max([1]))   # returns 1, 1

print(get_min_max(None))   # returns None

