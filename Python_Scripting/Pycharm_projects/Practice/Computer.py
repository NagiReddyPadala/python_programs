class Computer:
    wheels = 4
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def congfig(self):
        print("Config is: ", self.cpu, self.ram)

    def add(self, a, b):
        return a+b

    def add(self, a, b, c):
        return a+b+c


comp1 = Computer("i5", "8GB")
comp2 = Computer('i7', '16GB')
a = 1
b = '1'
print(type(a))
print(type(b))
print(type(comp1))

#Computer.congfig(comp1)
comp1.congfig()
comp2.congfig()
print(id(comp1))
print(id(comp2))

print(comp1.wheels)
print(comp2.wheels)

x = 1
print(id(x))
x = "Nagi"
print(id(x))

print(comp1.add(1,2,3))