def digits_sum(num):
    result = 0
    #Initializes result to 0
    strnum= str(num)
    #Changes the value of the number from an integer to a string
    for char in strnum:
        #This iterates over each character in the string assigned to 'strnum'
        result += int(char)
        #For every character in the string, it is convered to an integer
        #and added to result, thereby adding all the characters together
    return ("Sum of the digits in "+str(num)+ " is: "+str(result))

print(digits_sum(1234))
print(digits_sum(456783))