student = {'name': "Nagi",
           'age': 30,
           'courses' : ['python', 'c']}


print(student.get('nadame'), 'Not found')
print(student.get('name'), 'Not found')
print(student.get('name'))
print(student['age'])


student['phone'] = '9538226549'
print(student)

student.update({'name': 'Madhu', 'phone': '7093884784'})
print(student)

del student['age']
print(student)

phone = student.pop('phone')

print(phone)
print(student)

print(len(student))
print(student.values())
print(student.keys())
print(student.items())


for key in student:
    print(key)

for key, val in student.items():
    print(key, " - ", val)