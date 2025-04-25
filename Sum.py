def sum_all (*args):
    """
    This calculates the sum of all numbers
    passed as arguments in the function as parameters
    """
    total=0
    #Initializes the total to 0
    for arg in args:
        if isinstance(arg, list):
            total += sum(arg)
            #If the parameter is a list(array), each element should be added
        else:
            total += arg
            #Sums all the values passed as individual parameters
    return total

print(sum_all(1,2,3,4,5))
print(sum_all(4.5, 1.3, 2.2, 1.7, 0.9))

numbers=[2,4,6,8,10,12]
print(sum_all(numbers))
#The asterisk symbol "*" is used to unpack elements in a list/array