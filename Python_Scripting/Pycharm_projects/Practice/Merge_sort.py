lst = [5,8,4,9,1,2,11,21,31,41,51,61,71,81]
print("list length: ", len(lst) )

def merge_sort(lst):
    devide_and_merge(lst, 0, len(lst) -1)
    return  lst

def devide_and_merge(lst, first, last):
    if first < last:
        mid = (first + last) // 2
        devide_and_merge(lst, first, mid)
        devide_and_merge(lst, mid+1, last)
        merge(lst, first, mid, last)

def merge(lst, first, mid, last):
    left = lst[first:mid+1]
    right = lst[mid+1:last+1]
    #left.append(999999999)
    #right.append(999999999)
    i = j = 0
    for k in range(first, last+1):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                lst[k] = left[i]
                #print("i, j: ", i, j)
                i += 1
            else:
                lst[k] = right[j]
                j += 1


print(merge_sort(lst))
