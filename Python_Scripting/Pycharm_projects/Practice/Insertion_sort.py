lst = [7, 8, 5, 4, 9, 2]
print(lst)
def insertion_sort(lst):

    for i in range(1, len(lst)):
        curr_num = lst[i]
        for j in range(i-1, -1, -1):
            if lst[j] > curr_num:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


print(insertion_sort(lst))