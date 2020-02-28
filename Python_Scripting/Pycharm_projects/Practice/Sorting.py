vals = [3,5,2,9,7,10]

for j in range(len(vals)):
    for i in range(len(vals)-1):
        if vals[i] > vals[i+1]:
            vals[i], vals[i+1] = vals[i+1], vals[i]

print(vals)
print(vals[len(vals)-1])


def add_sub(x,y):
    sum = x+y
    diff = x-y
    return sum, diff

res1,res2 = add_sub(6,1)
print(res1, res2)