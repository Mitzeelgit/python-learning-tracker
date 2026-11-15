def factorial():
    number = 4
    result = 1
    while (number > 0):
        result = result * number
        number -= 1

    return result

print(factorial())
