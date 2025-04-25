def factorial(num):
    """
    This function takes the number passed as a parameter and
    calculates its factorial using recursion
    """
    if num == 1:
        return 1
    #This sets 1 as the base case for the recursion
    else:
        result = num * factorial(num-1)
    #If num is not 1, then the function will multiply num with another
    #instance of the same function by calling itself again but with the parameter minus 1
    return result


print(factorial(7))
print(factorial(10))
