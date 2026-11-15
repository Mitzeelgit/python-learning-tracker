def checkprime():
    isprime = True
    n = 14
    if n <= 1:
        isprime = False
    else:
        for i in range(2,n):
            if n%i == 0:
                isprime = False
                break

    return isprime

print(checkprime())

