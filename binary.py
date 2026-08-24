def binary():
    binary_num = (input("Enter a binary number \n"))

    reversed = binary_num[::-1]

    decimal_value = 0

    for position,digit in enumerate(reversed):
        if digit == '1':
            decimal_value += 2**position

    print(decimal_value)

binary()