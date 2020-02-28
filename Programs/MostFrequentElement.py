lst  = [1, 2, 3, 4, 2, 3, 2, 3]

def most_frequent(lst):
    count = 0
    num = None
    for i in lst:
        frq = lst.count(i)
        if frq > count:
            count = frq
            num = i
    return num, count

def most_frequent1(List):
    dict = {}
    count, itm = 0, ''
    for item in List:
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count :
            count, itm = dict[item], item
    return(itm)

# Program to find most frequent
# element in a list
def most_frequent2(List):
    return max(set(List), key = List.count)

num, count  = most_frequent(lst)
print("Most frequent number: {}, count {}".format(num, count))
print(most_frequent1(lst))
print(most_frequent2(lst))