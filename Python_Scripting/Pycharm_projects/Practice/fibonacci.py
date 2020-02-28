num = 20

print(0, end=" ")
print(1, end=" ")

prev = 0
curr = 1
for i in range(2, num):
    sum = prev + curr
    prev = curr
    curr = sum
    if sum > 100:
        break
    print(sum, end=" ")

