def fibonacci(n):
    a = 0
    b = 1

    if n < 0:
        return "Invalid Input"
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b


def rec_fibonacci(n):
    if (n < 0):
        return  "Invalid Input"
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fibonacci(n-1) + rec_fibonacci(n-2)


print(fibonacci(2))

for i in range(0, 11):
    print(fibonacci(i), end= " ")

print()

for i in range(0, 11):
    print(rec_fibonacci(i), end=" ")