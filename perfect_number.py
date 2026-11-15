def perfect_number():
    n = 400
    proper_divisors = []
    answer = True
    sum = 0

    for i in range(1,n):
        if n%i == 0:
            proper_divisors.append(i)

    for numbers in proper_divisors:
        sum = sum + numbers

    if sum != n:
        return False

    return answer

print(perfect_number())
