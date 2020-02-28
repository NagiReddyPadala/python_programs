
def rec_fact(n):
    return 1 if n == 0 or n == 1 else n*fact(n-1)

def fact(n):
    if n < 0:
        return "Invalid input"
    elif n == 0 or n == 1:
        return 1
    else:
        res = 1
        for i in range(2, n+1):
            res *= i
        return res

print(fact(0))
print(fact(1))
print(fact(2))
print(fact(5))

print()

print(rec_fact(0))
print(rec_fact(1))
print(rec_fact(2))
print(rec_fact(5))