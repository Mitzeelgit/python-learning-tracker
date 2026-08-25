import math

ask_options = ['ADDITION','SUBTRACTION','DIVISION','MULTIPLICATION','EXPONENTIAL','SQUARERT','CUBERT','FACTORIAL','ABS']

ask = ''
print("WELCOME TO CALCULATOR \n TYPE THE OPERATION YOU WANT TO DO")
while ask not in ask_options:
    ask = input("------CALCULATOR------ \n ADDITION : Type to Add \n SUBTRACTION : Type To Subtract \n DIVISON : Type To Divide \n MULTIPLICATION : Type To Multiply \n EXPONENTIAL : Type For Exponent \n SQUARERT : Type For Square Root \n CUBERT : Type For Cube Root \n ABS : Type For Absoulute Value \n FACTORIAL : Type For Factorial\n").upper()

    if ask not in ask_options:
        print("Choose one of the above calculation")


if ask == 'ADDITION'.upper():

    user_input = input("Enter all numbers with a space : \n -- eg : 10 20 30 \n")

    numbers_str = user_input.split()

    total = 0.0

    for numbs in numbers_str:
        total += float(numbs)

    print("Sum Of Your Numbers Is : {}".format(total))
    
if ask == 'SUBTRACTION'.upper():

    user_input = input("Enter all numbers with a space : \n -- eg 10 20 30 \n")

    numbers_str = user_input.split()

    if numbers_str:
        numbers = [float(num) for num in numbers_str]

        total_sub = numbers_str[0]

        for num in numbers[1:]:
            total_sub -= num

    print("Subtraction of your numbers is {}".format(total_sub))

if ask == 'MULTIPLICATION'.upper():

    user_input = input("Enter all numbers with a space. \n --eg 10 20 30 \n")

    numbers_str = user_input.split()

    total = 1

    for num in numbers_str:
        total = total*float(num)


    print("Multiplication of your numbers are {}".format(total))

if ask == 'DIVISION'.upper():

    user_input = input("Enter all numbers with a space. \n --eg number to be divided , by which number \n")
    
    numbers_str = user_input.split()

    numbers = [float(num) for num in numbers_str]

    if len(numbers) == 0:
        print("You did not enter any numbers.")
    else:
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Error: Cannot divide by zero.")
                break
            result /= num
        else:
            print(f"The final division result is: {result}")

if ask == 'EXPONENTIAL'.upper():

    user_input = float(input("Enter the number you want to find the exponent of --eg 10"))

    expo = math.e**(user_input)

    print("Exponential value of your number is {}".format(expo))

if ask == 'SQUARE RT'.upper():

    user_input = float(input("Enter the number you want square root of --eg 10"))

    sqrt = user_input**(0.5)

    print("Square root of your number is {}".format(sqrt))

if ask == 'CUBERT'.upper():
    
    user_input = float(input("Enter the number you want cube root of --eg 10"))

    cubert = user_input**(0.5)

    print("Cube root of your number is {}".format(cubert))

if ask == 'ABS'.upper():

    user_input = float(input("Enter the number you want absolute value of --eg 10"))

    absval = abs(user_input)

    print("Absolute value of your number is {}.".format(absval))

if ask == 'FACTORIAL'.upper():

    user_input = float(input("Enter the value of factorial that you want --eg 10 \n"))

    totalfact = 1

    while user_input > 0:
        totalfact *= user_input

        user_input -= 1

    print("Factorial is {}".format(totalfact))


