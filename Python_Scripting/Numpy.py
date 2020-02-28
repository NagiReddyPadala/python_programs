import numpy as np

#Creating a rank 1 array
arr = np.array([1, 2, 3])
print("Array with rank 1: \n", arr)


#Creating a rank 2 array
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print("Array with rank 2: \n", arr)

print(type(arr))



#Creating a rank 1 array from tuple
arr = np.array((1, 2, 3))
print("Array with rank 1 using tuple: \n", arr)



print(type(arr))


arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16]])

sliced_arr = arr[:2, ::2]


Indexed_arr = arr[[0, 1, 2, 3],
                   [0, 1, 2, 3]]

print(arr)
print(sliced_arr)
print(Indexed_arr)

print("after changing")
sliced_arr[0][0] = 1111
print(sliced_arr[0][0])

print(arr)
print(sliced_arr)
print(Indexed_arr)




print(id(arr))
print(id(sliced_arr))
print(id(Indexed_arr))


a = np.array([[1, 2],
              [3, 4]])

b= np.array([[5, 6],
             [7, 8]])

print("adding 1 to each element of a: \n", a+1)
print("subtracting 2 from each element of b: \n", b-2)
print("Adding all the elements of a: \n", a.sum())
print("Adding elements of a and b: \n5", a+b)



x = np.array([1, 2])
print(x.dtype)

x = np.array([1.0, 2.0])
print("Datatype: ", x.dtype)
print("Array type: ", type(x))



x = np.array([1, 2], dtype= np.int64)
print(x.dtype)
print(x)


y = np.array([[1, 2],
            [3, 4]])
z = np.array([[5, 6],
            [7, 8]])

print(y)
print(z)

addition = np.add(y, z)
print("Addition: \n", addition)

arrSum = np.sum(y)
print("Sum of Y: \n", arrSum)

arrSqrt = np.sqrt(z)
print("Sqrt of Z: \n", arrSqrt)

print("Transpose of Y: \n", y.T)

y = np.array([[[1, 2, 3, 4],
            [3, 4, 5, 6]],
              [[1, 2, 3, 4],
            [3, 4, 5, 6]]])


print("Type: ", type(y))
print("Axes: ", y.ndim)
print("shape: ", y.shape)
print("Size: ", y.size)
print("DType: ", y.dtype)


# Creating array from list with type float
a = np.array([[1, 2, 4], [5, 8, 7]], dtype = 'float')
print ("Array created using passed list:\n", a)
 
# Creating array from tuple
b = np.array((1 , 3, 2))
print ("\nArray created using passed tuple:\n", b)

c = np.zeros((2, 3, 4))
print(c)
print(c[0][0][0])
d = np.full((3,3), 6, dtype= 'complex')
print(d)


# An exemplar array
arr = np.array([[-1, 2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])

print(arr[arr>2])

print("Maximum: ", arr.max())
print("Shape: ", arr.shape)
print("column wise max: ", arr.max(axis=0))
print("Row wise min: ", arr.min(axis=1))
print("column-wise cumulative Sum: ", arr.cumsum(axis=0))



a = np.array([[1, 2],
            [3, 4]])
b = np.array([[4, 3],
            [2, 1]])

print("Matrix multiplication: \n", a.dot(b))


# create an array of sine values
a = np.array([0, np.pi/2, np.pi])
print ("Sine values of array elements:", np.sin(a))
 
# exponential values
a = np.array([0, 1, 2, 3])
print ("Exponent of array elements:", np.exp(a))
 
# square root of array values
print ("Square root of array elements:", np.sqrt(a))


a = np.array([1, 2, 3])
dt = a.dtype
print("DataType: ", dt.name)
print("Data size: ", dt.itemsize)
print("Endian type: ", dt.byteorder)



b = np.empty(2, dtype = int)
print("Matrix b : \n", b)
 
a = np.empty([2, 2], dtype = int)
print("\nMatrix a : \n", a)
 
c = np.empty([3, 3])
print("\nMatrix c : \n", c)



array = np.arange(8)
print("Original array : \n", array)
 
# shape array with 2 rows and 4 columns
array = np.arange(8).reshape(2, 4)
print("\narray reshaped with 2 rows and 4 columns : \n", array)
 
# shape array with 4 rows and 2 columns
array = np.arange(8).reshape(4 ,2)
print("\narray reshaped with 4 rows and 2 columns : \n", array)
 
# Constructs 3D array
array = np.arange(8).reshape(2, 2, 2)
print("\nOriginal array reshaped to 3D : \n", array)



# restep set to True
print("B\n", np.linspace(2.0, 3.0, num=5, retstep=True), "\n")
 
# To evaluate sin() in long range 
x = np.linspace(0, 2, 10)
print("X: ", x)
print("A\n", np.sin(x))


array = np.array([[1, 2], [3, 4]])
 
# using flatten method
print(array.flatten())
 
#using fatten method 
#array.flatten('F')
print(array.flatten('F'))


a = np.array([1])
 
print("type is: ",type(a))
print("dtype is: ",a.dtype)



 
# A structured data type containing a
# 16-character string (in field ‘name’) 
# and a sub-array of two 64-bit floating
# -point number (in field ‘grades’)
 
dt = np.dtype([('name', np.unicode_, 16),
               ('grades', np.float64, (2,))])
# Data type of object with field grades
print(dt['grades'])
 
# Data type of object with field name 
print(dt['name'])

x = np.array([('Nagi', (6.00, 7.5)),
              ('Madhu', (7.55, 8.12))], dtype=dt)

print("Grades of Nagi: ", x[0]['grades'])
print("Names are: ", x['name'])


# NumPy array with elements from 1 to 9
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
 
# Index values can be negative.
arr = x[[1, 3, -3]]
print("\n Elements are : \n",arr)



import numpy as np
 
a = np.array([[0 ,1 ,2],
              [3 ,4 ,5 ],
              [6 ,7 ,8],
              [9 ,10 ,11]])
 
print(a[1:2 ,1:3 ])
print(a[1:2 ,[1,2]])


# You may wish to select numbers greater than 50
import numpy as np
 
a = np.array([10, 40, 80, 50, 100])
print(a[a>50])
print(a[a%40==0]**2)


# You may wish to select those elements whose
# sum of row is a multiple of 10.
import numpy as np
 
b = np.array([[5, 5],
              [4, 5],
              [16, 4]])
sumrow = b.sum(-1)
print(type(sumrow))
print(sumrow)

print(sumrow.shape)
print(b[sumrow%10==0])
print(b[sumrow%10==0].shape)


print("************************************************")
a = np.array([[0 ,1 ,2],
              [3 ,4 ,5 ],
              [6 ,7 ,8],
              [9 ,10 ,11]])

b = a.T

#for x in np.nditer(a):
#    print(x, end=" ")

for x in np.nditer(b, order="C"):
    print(x, end=" ")


for x in np.nditer(b, op_flags = ["readwrite"]):
    x[...] = 5*x
print(b)

for x in np.nditer(b, flags = ['external_loop'], order = 'C'):
    print(x)



# Python program explaining
# bitwise_and() function
 
import numpy as geek
in_num1 = 10
in_num2 = 11
 
print ("Input  number1 : ", in_num1)
print ("Input  number2 : ", in_num2) 
   
out_num = geek.bitwise_and(in_num1, in_num2) 
print ("bitwise_and of 10 and 11 : ", out_num) 

in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
  
print ("Input array1 : ", in_arr1) 
print ("Input array2 : ", in_arr2)
   
out_arr = geek.bitwise_and(in_arr1, in_arr2) 
print ("Output array after bitwise_and: ", out_arr) 



in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
  
print ("Input array1 : ", in_arr1) 
print ("Input array2 : ", in_arr2)
   
out_arr = geek.bitwise_or(in_arr1, in_arr2) 
print ("Output array after bitwise_or: ", out_arr)


# Python program explaining
# bitwise_xor() function
 
import numpy as geek
 
in_arr1 = [2, 8, 125]
in_arr2 = [3, 3, 115]
  
print ("Input array1 : ", in_arr1) 
print ("Input array2 : ", in_arr2)
   
out_arr = geek.bitwise_xor(in_arr1, in_arr2) 
print ("Output array after bitwise_xor: ", out_arr)



# Python program explaining
# packbits() function
import numpy as np
 
# creating an array using 
# array function
a = np.array([[[1,0,1],
             [0,1,0]],
             [[1,1,0],
             [0,0,1]]])
 
# packing elements of an array
# using packbits() function
b = np.packbits(a, axis=-1)
 
print(b)



# Python program explaining
# unpackbits() function
import numpy as np
 
# creating an array using 
# array function
a = np.array([[2], [7], [23]], dtype=np.uint8)
 
# packing elements of an array
# using packbits() function
b = np.unpackbits(a, axis = 1)
 
print(b)



# Python program explaining
# numpy.lower() function
 
import numpy as np
 
# converting to lowercase
print(np.char.lower(['GEEKS', 'FOR']))
 
# converting to lowercase
print(np.char.lower('GEEKS'))


# Python program explaining
# numpy.split() function
 
import numpy as np
 
# splitting a string
print(np.char.split('geeks for geeks'))
 
# splitting a string
print(np.char.split('geeks, for, geeks', sep = ','))



# Python program explaining
# numpy.join() function
 
import numpy as np
 
# splitting a string
print(np.char.join('-', 'geeks'))
 
# splitting a string
print(np.char.join(['-', ':'], ['geeks', 'for']))



a=np.array(['geeks', 'for', 'geeks'])
 
# counting a substring
print(np.char.count(a,'geek'))
 
# counting a substring
print(np.char.count(a, 'fo'))





import numpy as np
 
a=np.array(['geeks', 'for', 'geeks'])
 
# counting a substring
print(np.char.rfind(a,'geek'))
 
# counting a substring
print(np.char.count(a, 'fo'))


# counting a substring
print(np.char.isnumeric('geeks'))
 
# counting a substring
print(np.char.isnumeric('12geeks'))


 
# comparing a string elementwise
# using equal() method
a=np.char.equal('geeks','for')
 
print(a)


# comparing a string elementwise
# using unequal() method
a=np.char.not_equal('geeks','for')
 
print(a)



 
# comparing a string elementwise
# using greater() method
a=np.char.greater('geeks','for')
 
print(a)



# Importing numpy as np
import numpy as np
 
A = np.array([[6, 1, 1, 2],
              [4, -2, 5, 2],
              [2, 8, 7, 2]])
 
# Rank of a matrix
print("Rank of A:", np.linalg.matrix_rank(A))
 
# Trace of matrix A
print("\nTrace of A:", np.trace(A))
 
# Determinant of a matrix
#print("\nDeterminant of A:", np.linalg.det(A))
 
# Inverse of matrix A
#print("\nInverse of A:\n", np.linalg.inv(A))
 
#print("\nMatrix A raised to power 3:\n",
#           np.linalg.matrix_power(A, 3))


# importing libraries
import numpy as np
 
# sort along the first axis
a = np.array([[12, 15], [10, 1]])
arr1 = np.sort(a, axis = 0)        
print ("Along first axis : \n", arr1)        
 
 
# sort along the last axis
a = np.array([[10, 15], [12, 1]])
arr2 = np.sort(a, axis = -1)        
print ("\nAlong first axis : \n", arr2)
 
 
a = np.array([[12, 15],
              [10, 1]])
arr1 = np.sort(a, axis = -1)        
print ("\nAlong none axis : \n", arr1)




# Numpy array created
a = np.array([9, 3, 1, 7, 4, 3, 6])
 
# unsorted array print
print('Original array:\n', a)
 
# Sort array indices
b = a.argsort()
print ("Arg sort: ", b)

c = np.zeros(len(b), dtype=int)
print(c)

for x in range(0,len(b)):
    c[x] = a[b[x]]

print('Sorted array->', c)


# Numpy array created
# First column
a = np.array([9, 3, 1, 3, 4, 3, 6])
 
# Second column 
b = np.array([4, 6, 9, 2, 1, 8, 7]) 
print('column a, column b')

for i, j in zip(a, b):
    print(i, " ", j)


c = np.lexsort((b,a))
print(c)


import numpy as geek 
 
# Working on 2D array
array = geek.arange(12).reshape(3, 4)
print("INPUT ARRAY : \n", array)
 
# No axis mentioned, so works on entire array
print("\nMax element : ", geek.argmax(array))
 
# returning Indices of the max element
# as per the indices
print(("\nIndices of Max element : "
      , geek.argmax(array, axis=0)))
print(("\nIndices of Max element : "
      , geek.argmax(array, axis=1)))



 
import numpy as geek 
 
# Working on 1D array
array = [geek.nan, 4, 2, 3, 1]
print("INPUT ARRAY 1 : \n", array)
 
array2 = geek.array([[geek.nan, 4], [1, 3]])
 
# returning Indices of the max element
# as per the indices ingnoring NaN
print(("\nIndices of max in array1 : "
       , geek.nanargmax(array)))
 
# Working on 2D array
print("\nINPUT ARRAY 2 : \n", array2)
print(("\nIndices of max in array2 : "
      , geek.nanargmax(array2)))
 
print(("\nIndices at axis 1 of array2 : "
      , geek.nanargmax(array2, axis = 1)))


import numpy as geek 
 
# Working on 1D array
array = geek.arange(8)
print("INPUT ARRAY : \n", array)
 
 
# returning Indices of the min element
# as per the indices
print("\nIndices of min element : ", geek.argmin(array, axis=0))


import numpy as np
  
# Counting a number of 
# non-zero values
a = np.count_nonzero([[0,1,7,0,0],
                      [3,0,0,2,19]])
b = np.count_nonzero(([[0,1,7,0,2],[3,0,0,0,19]])
                     , axis=0)
 
print("Number of nonzero values is :", a)
print("Number of nonzero values is :", b)



dtypes = [('name', 'S10'), ('grad_year', int), ('cgpa', float)] 
  
# Values to be put in array 
values = [('Hrithik', 2009, 8.5), ('Ajay', 2008, 8.7),  
           ('Pankaj', 2008, 7.9), ('Aakash', 2009, 9.0)] 
             
# Creating array 
arr = np.array(values, dtype = dtypes) 
print ("\nArray sorted by names:\n", 
            np.sort(arr, order = 'name')) 
              
print ("Array sorted by grauation year and then cgpa:\n", 
                np.sort(arr, order = ['grad_year', 'cgpa']))


import numpy as np 
  
a = np.array([[1, 2], 
              [3, 4]]) 
  
b = np.array([[5, 6], 
              [7, 8]]) 

print(a)
print(b)
# vertical stacking 
print("Vertical stacking:\n", np.vstack((a, b))) 
  
# horizontal stacking 
print("\nHorizontal stacking:\n", np.hstack((a, b))) 
  
c = [11, 12] 
  
# stacking columns 
print("\nColumn stacking:\n", np.column_stack((a, c))) 
  
# concatenation method  
print("\nConcatenating to 2nd axis:\n", np.concatenate((a, b), 1))



a = np.array([[1, 3, 5, 7, 9, 11], 
              [2, 4, 6, 8, 10, 12]]) 
  
# horizontal splitting 
print("Splitting along horizontal axis into 2 parts:\n", np.hsplit(a, 3)) 
  
# vertical splitting 
print("\nSplitting along vertical axis into 2 parts:\n", np.vsplit(a, 2))


import numpy as np 
  
a = np.array([1.0, 2.0, 3.0]) 
  
# Example 1 
b = 2.0
print(a * b) 
  
# Example 2 
c = [2.0, 2.0, 2.0] 
print(a * c)


a = np.array([0.0, 10.0, 20.0, 30.0]) 
b = np.array([0.0, 1.0, 2.0]) 
  
print(a[:, np.newaxis] + b)

myDate = np.datetime64("2020-01-01")
print("Date: ", myDate)
print("Year: ", np.datetime64(myDate, 'Y'))

febDates = np.arange("2020-02", "2020-03", dtype="datetime64[D]")
print(febDates)


dur = np.datetime64('2017-05-22') - np.datetime64('2016-05-22') 
print("\nNo. of days:", dur) 
print("No. of weeks:", np.timedelta64(dur, 'W')) 

# sorting dates 
a = np.array(['2017-02-12', '2016-10-13', '2019-05-22'], dtype='datetime64') 
print("\nDates in sorted order:", np.sort(a))


import numpy as np 
import matplotlib.pyplot as plt 
  
# x co-ordinates 
x = np.arange(0, 9) 
A = np.array([x, np.ones(9)]) 
  
# linearly generated sequence 
y = [19, 20, 20.5, 21.5, 22, 23, 23, 25.5, 24] 
# obtaining the parameters of regression line 
w = np.linalg.lstsq(A.T, y)[0]  
  
# plotting the line 
line = w[0]*x + w[1] # regression line 
#plt.plot(x, line, 'r-') 
#plt.plot(x, y, 'o') 
#plt.show()


import numpy as np 
  
# function to print Checkerboard pattern 
def printcheckboard(n): 
      
    print("Checkerboard pattern:") 
    # create a n * n matrix 
    x = np.zeros((n, n), dtype = int) 
    # fill with 1 the alternate rows and columns 
    x[1::2, ::2] = 1
    x[::2, 1::2] = 1
      
    # print the pattern 
    for i in range(n): 
        for j in range(n): 
            print(x[i][j], end =" ")  
        print()  
  
# driver code 
n = 8
printcheckboard(n) 

