def egyptianMultiplication(a, b):
    acc = 0
    power = 1
    while a:
        acc += (a & 1) * power * b
        a >>= 1
        power <<= 1
    return acc



numberA = int(input())
numberB = int(input())

print("La multiplication egyptienne de {} par {} est {}".format(numberA, numberB, egyptianMultiplication(numberA, numberB)))