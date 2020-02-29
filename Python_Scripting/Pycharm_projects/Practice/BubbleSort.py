lst = [5,8,4,9,1,2,11,21,31,41,51,61,71,81,91]

def sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i -1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
        print(lst)


print(lst)
sort(lst)
print(lst)
