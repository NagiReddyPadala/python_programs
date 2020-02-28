lst = [5,8,4,9,1,2,11,21,31,41,51,61,71,81,91]

def sort(lst):

    for i in range(len(lst)):
        min_pos = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_pos]:
                min_pos = j

        lst[i], lst[min_pos] = lst[min_pos], lst[i]
        print(lst)


print(lst)
print("************************************************")
sort(lst)
print("************************************************")
print(lst)

# def sort(lst):
#     for iteration in range(len(lst)):
#         min_pos = iteration
#         for index in range(iteration + 1, len(lst)):
#             if lst[index] < lst[min_pos]:
#                 min_pos = index
#
#         lst[iteration], lst[min_pos] = lst[min_pos], lst[iteration]
#         print(lst)