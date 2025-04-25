def digits_sum(num):
    result = 0
    strnum= str(num)
    for char in strnum:
        result += int(char)
    return ("Sum of the digits in "+str(num)+ " is: "+str(result))

print(digits_sum(1234))
print(digits_sum(456783)) 