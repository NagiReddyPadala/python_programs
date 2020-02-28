# lst = [1, 2, 3, 4]
#
# it = iter(lst)
# print(it.__next__())
# print(next(it))
#
# #for val in lst:
# for val in it:
#     print(val)

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

myTopTen = TopTen()
print(next(myTopTen))
print(myTopTen.__next__())
for num in myTopTen:
    print(num)


