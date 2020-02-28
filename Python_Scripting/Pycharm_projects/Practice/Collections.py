# Python 3 code to demonstrate
# removing duplicated from list
# using collections.OrderedDict.fromkeys()
from collections import OrderedDict

# initializing list
test_list = [1, 5, 3, 6, 3, 5, 6, 1]
print ("The original list is : " + str(test_list))

# using collections.OrderedDict.fromkeys()
# to remove duplicated
# from list
res = list(OrderedDict.fromkeys(test_list))

# printing list after removal
print("The list after removing duplicates : " + str(res))



#Named tuple

from collections import namedtuple

Color = namedtuple('Color', ['Red', 'Green', 'Blue'])
white =  Color(255, 255, 255)
print(white)
print(white.Red)

from collections import deque

a = ['n', 'a', 'g', 'i']
d = deque(a)
print(d)
d.appendleft('P')
print(d)
d.popleft()
print(d)

from collections import ChainMap
a = {1: 'One', 2: 'Two'}
b = {3: 'Three', 4: 'Four'}

c = ChainMap(a, b)
print(c)


from collections import Counter
a = [1,1,2,2,2,3,3,3,4,4,4,4,4,4]
c = Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub = {2:1, 4:2}
print(c.subtract(sub))
print(c.most_common())


#Ordered dictionary
d = OrderedDict()
d[1] = 'N'
d[2] = 'a'
d[3] = 'g'
d[4] = 'i'

print(d)
print(d.keys())
d[1] = 'n'
print(d)


#Defaultdict
from collections import defaultdict

