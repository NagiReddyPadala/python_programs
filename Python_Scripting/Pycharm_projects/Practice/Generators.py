
def topTen():
    num = 1
    while num <= 10:
        yield num*num
        num +=1

vals = topTen()

vals.__next__()
next(vals)
print(type(vals))

for val in vals:
    print(val)
