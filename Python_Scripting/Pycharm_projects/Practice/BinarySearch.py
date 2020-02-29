lst = [5,8,4,9,1,2,11,21,31,41,51,61,71,81,91]
n = 1
pos = -1
def search(lst, n):
    global pos
    lst.sort()
    print(lst)

    l = 0
    u = len(lst) - 1

    while l <= u:
        pos += 1
        mid = (l+u) // 2
        if n == lst[mid]:
            return True
        else:
            if n > lst[mid]:
                l = mid + 1
            else:
                u = mid -1

    return False

if search(lst, n):
    print("Found at position: ", pos)
else:
    print("Not found")