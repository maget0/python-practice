def factorial(num):
    """
    The function calculates the factorial of the number passed as a
    parameter using a for-loop
    """
    result = 1
    #Setting the value of result as 1 for multiplication

    for i in range(num,0,-1):
        """
        The for loop picks numbers in the range between 0 and the
        number whose factorial is to be calculated. Starting from the parameter
        value, the number is multiplied by the result and is stored as the
        new value for result, and the parameter is then subtracted by 1.
        The process repeats until num = 1
        """
        result *= i
    return result


factorial(5)
factorial(10)
factorial(3)
