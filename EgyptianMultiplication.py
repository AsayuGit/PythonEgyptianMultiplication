def egyptianMultiplication(a, b):
    acc = 0
    bAcc = b
    while a:
        if (a & 1)
            acc += bAcc
        a >>= 1
        bAcc <<= 1
    return acc



numberA = int(input())
numberB = int(input())

print("La multiplication egyptienne de {} par {} est {}".format(numberA, numberB, egyptianMultiplication(numberA, numberB)))