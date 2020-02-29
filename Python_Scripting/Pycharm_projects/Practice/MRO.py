# class X():
#     def who_am_i(self):
#         print("I am a X")
#
#
# class Y():
#     def who_am_i(self):
#         print("I am a Y")
#
#
# class A(X, Y):
#     def who_am_i(self):
#         print("I am a A")
#
#
# class B(Y, X):
#     def who_am_i(self):
#         print("I am a B")
#
#
# class F(A, B):
#     def who_am_i(self):
#         print("I am a F")
#
#
# f = F()
# print(help(f))
# #f.who_am_i()

# class A:
#     def process(self):
#         print('A process()')
#
#
# class B(A):
#     def process(self):
#         print('B process()')
#
# class C(A):
#     def process(self):
#         print('C process()')
#
# class D(A, C):
#     pass


class A:
    def process(self):
        print('A process()')

class B(A):
    pass

class C(A):
    def process(self):
        print('C process()')

class D(B, C):
     pass

obj = D()
obj.process()