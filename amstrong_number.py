def checkamstrong():

    isamstrong = True
    number_oringal = 153
    number = 153
    sum = 0
    number_of_digits = len(str(number))

    while number > 0:

        digit = number%10

        number = number // 10

        sum = digit**number_of_digits + sum

    if sum != number_oringal:
        isamstrong = False

    return isamstrong

print(checkamstrong())