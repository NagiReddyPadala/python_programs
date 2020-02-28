
f1 = open("favorites.PNG", 'rb')
f2 = open("favorites_copy.PNG", 'wb')

for data in f1:
    f2.write(data)

f1.close()
f2.close()