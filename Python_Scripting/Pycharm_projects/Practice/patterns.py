
# for i in range(1,5):
#     #for j in range(1,5):
#     #for j in range(0, i):
#     for j in range(0, 5-i):
#         #print("#", end=" ")
#         print(j+1, end=" ")
#     print()

x,y='ABCD','PQR'
for i in range(4):
    print(x[:i+1]+y[i:])

