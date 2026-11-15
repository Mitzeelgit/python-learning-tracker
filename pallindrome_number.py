def checkpallindrome():
    n = 121
    ispallindrome = True
    numbers = []

    if n < 0:
        return False
    while (n>0):
        digit = n%10
        n = n // 10
        numbers.append(digit)

    for i in range(len(numbers)):
        if numbers[i] != numbers[-i-1]:
            return False

    return ispallindrome

print(checkpallindrome())


def checkpallindrome1():
    n = 123
    for i in range(len(str(n))):

        if str(n) == str(n)[::-1]:
            return True
        else:
            return False

print(checkpallindrome1())

