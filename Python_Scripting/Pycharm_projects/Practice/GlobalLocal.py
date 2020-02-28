a = 10

def change():
    global a
    a = a + 5
    print("func1 ", a)

def change1():
    #global a
    a =  5
    print("func2 ", a)

change()
print("outer ", a)
change1()

print("Value of a using nonlocal is : ", end="")


print("******************")
def outer():
    a = 5

    def inner():
        nonlocal a
        print(a)
        a = 10
        print(a)

    inner()
    print(a)


outer()