lst = [5,8,4,9,1,2,11,21,31,41,51,61,71,81,91]

def sort(lst):
    for iteration in range(len(lst)):
        for index in range(len(lst) - iteration -1):
            if lst[index] > lst[index+1]:
                lst[index], lst[index+1] = lst[index+1], lst[index]
        print(lst)

print(lst)
sort(lst)
print(lst)
