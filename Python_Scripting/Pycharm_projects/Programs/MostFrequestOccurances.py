# Program to find most frequent 
# element in a list 

def most_frequent(List):
    dict = {}
    count, itm = 0, ''
    for item in List:
        dict[item] = dict.get(item, 0) + 1
        if dict[item] >= count:
            count, itm = dict[item], item
    return(dict)

List = [2, 1, 2, 2, 1, 3, 1]
res_dict = most_frequent(List)

print(res_dict)
print(sorted(res_dict.items(), key= lambda res_dict:res_dict[1]))

sqrt = lambda x: x*x

print(sqrt(5))