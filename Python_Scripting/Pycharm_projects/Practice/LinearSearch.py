lst = [5,8,4,9,1,2]
n = 9
pos = -1
def search(lst, n):
    global pos

    for index, val in enumerate(lst):
        if val == n:
            pos = index
            return True

    return False

if search(lst, n):
    print("Found at position: ", pos)
else:
    print("Not found")