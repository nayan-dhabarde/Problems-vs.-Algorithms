def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number == 0:
        return 0

    if number == 1:
        return 1
    return find_sqrt(number, 0, number)

    pass

def find_sqrt(number, start, end):

    if start == end:
        return start - 1

    mid = (start + end) // 2

    square = mid * mid

    if square == number:
        return mid
    elif square < number:
        return find_sqrt(number, mid + 1, end)
    else:
        return find_sqrt(number, start, mid)


print ("Pass" if  (3 == sqrt(9)) else "Fail")   # prints Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")   # prints Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")  # prints Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")   # prints Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")  # prints Pass
print ("Pass" if  (5 == sqrt(20)) else "Fail")  # prints Fail