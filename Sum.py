def sum_all (*args):
    """
    This calculates the sum of all numbers
    passed as arguments in the function as parameters
    """
    total = sum(args)
    return total

print(sum_all(1,2,3,4,5))
print(sum_all(4.5, 1.3, 2.2, 1.7, 0.9))
