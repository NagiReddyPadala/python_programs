def smart_div(fun):
    def inner(a,b):
        if a < b:
            a, b = b,a
        return fun(a, b)
    return inner

@smart_div
def div(a,b):
    print(a/b)



# def customize_wish(func):
#     def inner_func():
#         res = func()
#         return "Hey Nagireddy, " + res
#     return inner_func
#
# #@customize_wish
# def wish():
#     return "Good morning"

#print(customize_wish(wish)())


def accept_args(person):
    def customize_wish(func):
        def inner_func(msg):
            res = func(msg)
            return person + " " + res
        return inner_func
    return customize_wish


#@accept_args("Hey Madhu")
def wish(msg):
    return msg

print(wish("Good night"))


def custom_sort(func):
    def inner_func(*args):
        print("In custom function")
        return func(args[0])
    return inner_func

my_sort = custom_sort(sorted)
print(my_sort([1, 5, 2, 6, 3]))

# f1 = accept_args("Hey Madhu")
# f2 = f1(wish)
# print(f2("Good night"))


#div = smart_div(div)
#div(2,4)


# Python code to illustrate
# Decorators with parameters in Python

# def decorator(*args, **kwargs):
#     print("Inside decorator")
#     def inner(func):
#         print("Inside inner function")
#         print("I like", kwargs['like'])
#         return func
#     return inner
#
# @decorator(like = "geeksforgeeks")
# def func():
#     print("Inside actual function")
#
# func()
