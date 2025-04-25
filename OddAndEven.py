def checker (num):
    """
    This function takes the number input as a parameter and divides
    it by 2. If the remainder is 0 then the number is even while if
    it is 1, the number is odd.
    """
    rem = num%2
    if rem==1:
        print("Number is odd")
    elif rem==0:
        print("Number is even")


checker(5)
checker(10)
checker(4)
checker(0)



