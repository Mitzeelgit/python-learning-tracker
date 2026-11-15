def largestdigit():

    number = 513

    largestdigit = number % 10

    while (number > 0):
        digit = number%10

        number = number // 10
        
        if digit > largestdigit:
            largestdigit = digit

    return largestdigit

print(largestdigit())