def reverseno():

    number = int(input("Enter your number \n"))
    reverse = 0
    sign = 1
    if number < 0:
        sign = -1
        number = -number

    while (number > 0):

        digit = number%10

        reverse = reverse*10 + digit

        number = number // 10

    result = reverse * sign

    return result

print(reverseno())