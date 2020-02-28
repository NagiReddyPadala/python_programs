message = "Hello world"

print(message)

print(message.lower())
print(message.upper())

print(message.count('Hello'))
print(message.count('l'))

print(message.find('l'))
print(message.find('world'))
print(message.find('Not'))

replacedStr = message.replace("world", "Universe")

print(replacedStr)

greeting = "Hello"
name = "Madhu"

message = greeting + ', ' +  name
print(message)
print("{}, {}. Welcome".format(greeting, name))
fstr = f'{greeting}, {name.upper()}. Welcome'

print(fstr)
print(dir(name))
print(help(str))

print(help(str.lower))