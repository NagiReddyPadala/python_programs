num = 6

for i in range(1, num+1):
    res = 1
    for j in range(1, i+1):
        res *= j
    print(res)


def fact(num):
    if num == 0:
        return  1
    else:
        return num*fact(num-1)


print("***************")

print(fact(5))
