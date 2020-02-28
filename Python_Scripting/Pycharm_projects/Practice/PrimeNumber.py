num = 10

for i in range(2, num//2):
    if num%i == 0:
        print("Not prime")
        break
else:
    print("Prime")