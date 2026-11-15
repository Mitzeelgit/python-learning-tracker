def count_prime():
    n = 6
    outputs = 0

    for i in range(2,n+1):
        isprime = True
        for j in range(2,i):
            if i%j == 0:
                isprime = False
                break

        if isprime:
            outputs += 1

    return outputs

print(count_prime())
                
