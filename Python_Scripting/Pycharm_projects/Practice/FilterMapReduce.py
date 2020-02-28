from functools import reduce

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lst)

even_nums = list(filter(lambda x : x%2==0, lst))
print(even_nums)

doubles = list(map(lambda x : x*2, even_nums))
print(doubles)

compress = reduce(lambda x,y : x+y, doubles)
print(compress)


# lst = list(map(lambda x : x*x, (a for a in range(10))))
# print(lst)