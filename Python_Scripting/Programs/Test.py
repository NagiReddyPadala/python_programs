def fast (items= []):
    items.append (1)
    return items

print (fast ())
print (fast ())


class Test(object):
    def __init__(self):
        self.x = 1
 
t = Test()
print (t.x)
print (t.x)
print (t.x)
print (t.x)
