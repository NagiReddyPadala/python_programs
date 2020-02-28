courses = ['History', 'Math', 'Science', 'Lang']

print(courses)
print(len(courses))
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])


courses.append('Art')
print(courses)

courses.insert(0, 'ComSci')
print(courses)

courses_lng = ['Telugu', 'English']

courses.extend(courses_lng)
print(courses)

courses.remove('Art')
print(courses)

popped = courses.pop()
print(popped)
print(courses)

courses.reverse()
print(courses)
print(sorted(courses))
courses.sort(reverse=True)
print(courses)

nums = [1, 2, 3, 4]
print(min(nums))
print(max(nums))
print(sum(nums))

print(courses.index('Telugu'))

for item in courses:
    print(item)

#for index, course in enumerate(courses):
for index, course in enumerate(courses,start=1):
    print("Index: {}, Course: {}".format(index, course))


courses_str = ", ".join(courses)
print(courses_str)

newCourses = courses_str.split(",")
print(newCourses)

list1 = ['Telugu', ' Science', ' Math', ' Lang', ' History', ' ComSci']
list2 = list1
print(id(list1))
print(id(list2))

print(list1)
print(list2)


list1[1] = 'English'

print(list1)
print(list2)

tuple1 = ('Telugu', ' Science', ' Math', ' Lang', ' History', ' ComSci')
tuple2 = tuple1

print(id(tuple1))
print(id(tuple2))

print(tuple1)
print(tuple2)

#tuple1[1] = 'English'
print("********************")
print(tuple1)
print(tuple2)


set1 = {'Telugu', ' Science', ' Math', ' Lang', ' History', ' ComSci', 'Math'}
set2 = {'Telugu', ' Science', ' Math', 'NewSub'}
print(set1.intersection(set2))
print(set1.union(set2))
print(set1)
#print(list1(set1))



empty_list = list()
empty_list = []

empty_tuple = tuple()
empty_tuple = ()

empty_set = set()
#empty_set = {}  This is wrong, it creates dictionary


list = [1,1,2,2,3,3,4,4]
set1 = set(list)
print(set1)
for item in set1:
    print(item)