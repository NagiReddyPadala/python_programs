# import pandas as pd
import pandas as pd
 
# list of strings
lst = ['Geeks', 'For', 'Geeks', 'is', 
            'portal', 'for', 'Geeks']
 
# Calling DataFrame constructor on list
df = pd.DataFrame(lst)
print(df)


lst = ["Hello", "Hi", "How", "are", "you"]
df = pd.DataFrame(lst)
print(df)



data = {'name': ['name1', 'name2', 'name3', 'name4'],
        'age': [20, 21, 22, 23],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

df = pd.DataFrame(data)
print(df[['name', 'Address']])
#print(type(df))


data = pd.read_csv("nba.csv", index_col = 'Name')
first = data.loc["Avery Bradley"]
second = data.loc["R.J. Hunter"]
third = data.iloc[0]

print(first, "\n\n\n", second, "\n\n\n", third)

print("*******************************")
age = data['Age']

print(age)


import numpy as np
# dictionary of lists
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, 56],
        'Third Score':[25, 40, 80, 98],
        'Fourth Score':[np.nan, np.nan, np.nan, 65]}
 
# creating a dataframe from list
df = pd.DataFrame(dict)
 
# using isnull() function  
print(df.isnull())
print("---------------------------------------")
print(df.notnull())
print("---------------------------------------")
print(df.fillna('0'))
print("---------------------------------------")
print(df.dropna())

# importing pandas as pd
import pandas as pd
  
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
# creating a dataframe from a dictionary 
df = pd.DataFrame(dict)
print(df)
print("---------------------------------------")
for i, j in df.iterrows():
    print (i, "\n", j)
    print("***************")
print("---------------------------------------")
# creating a list of dataframe columns
print(df)
columns = list(df)
print(columns)
print("---------------------------------------")
for i in columns:
 
    # printing the third element of the column
    print (df[i][2])


# Import pandas package  
import pandas as pd 
  
# Define a dictionary containing Students data 
data = {'Name': ['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Height': [5.1, 6.2, 5.1, 5.2], 
        'Qualification': ['Msc', 'MA', 'Msc', 'Msc']} 
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data) 
  
# Declare a list that is to be converted into a column 
address = ['Delhi', 'Bangalore', 'Chennai', 'Patna'] 
  
# Using 'Address' as the column name 
# and equating it to the list 
df['Address'] = address 
  
# Observe the result 
print(df) 



# importing pandas module 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name" ) 
  
# dropping passed columns 
data1 = data.drop(["Team", "Weight"], axis = 1, inplace = False) 
  
# display 
print(data)
print("--------------------------------------------------------------")
print(data1)
print("--------------------------------------------------------------")
print(list(data1))


# making data frame  
df = pd.read_csv("nba.csv", index_col ="Name")  
  
print(df.head(10))
  
new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3, 
                        'Position':'PG', 'Age':33, 'Height':'6-2', 
                        'Weight':189, 'College':'MIT', 'Salary':99999}, 
                                                            index =[0])

df = pd.concat([new_row, df], sort= False).reset_index(drop = True)
print("***********************************")
print(df.head(5))


# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name" ) 

# dropping passed values 
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter", "R.J. Hunter"], axis=0, inplace = True) 

# display 
print(data)


import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 

# retrieving multiple rows by loc method 
first = data.loc[["Avery Bradley", "R.J. Hunter"]] 

print("*********-------------*********************")

print(first) 


import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 

# retrieving two rows and three columns by loc method 
first = data.loc[["Avery Bradley", "R.J. Hunter"], 
				["Team", "Number", "Position"]] 



print(first)


import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 

# retrieving all rows and some columns by loc method 
first = data.loc[:, ["Team", "Number", "Position"]] 



print(first) 


import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 


# retrieving multiple rows by iloc method 
row2 = data.iloc [[3, 5, 7]] 



print(row2 )


import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 


# retrieving two rows and two columns by iloc method 
row2 = data.iloc [[3, 4], [1, 2]] 



print(row2)



# dictionary of lists 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict, index=[True, False, True, False])
print(df)
print(df.loc[True])
print(df.iloc[1])


df = pd.DataFrame(dict, index=[0, 1, 2, 3])
print(df[[True, False, True, True]])



# making data frame from csv file 
data = pd.read_csv("nba1.1.csv") 
   
df = pd.DataFrame(data, index = [0, 1, 2, 3, 4, 5, 6, 
                                 7, 8, 9, 10, 11, 12]) 
  
   
print(df[[True, False, True, False, True, 
    False, True, False, True, False, 
                True, False, True]] )


dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[90, 40, 80, 98]}

df = pd.DataFrame(dict)
print(df['degree'] == 'MBA')


# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba.csv", index_col ="Name") 

# using greater than operator for filtering of data 
print(data['Age'] > 25) 


# importing pandas as pd 
import pandas as pd 

# dictionary of lists 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
		'degree': ["BCA", "BCA", "M.Tech", "BCA"], 
		'score':[90, 40, 80, 98]} 


df = pd.DataFrame(dict, index = [0, 1, 2, 3]) 

mask = df.index == 0

print(df[mask]) 


# importing pandas as pd 
import pandas as pd 

# dictionary of lists 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
		'degree': ["BCA", "BCA", "M.Tech", "BCA"], 
		'score':[90, 40, 80, 98]} 


df = pd.DataFrame(dict, index = [0, 1, 2, 3]) 

mask = df.index == 0

print(df[mask]) 

# importing pandas package 
import pandas as pd 

# making data frame from csv file 
data = pd.read_csv("nba1.1.csv") 

# giving a index to a dataframe 
df = pd.DataFrame(data, index = [0, 1, 2, 3, 4, 5, 6, 
								7, 8, 9, 10, 11, 12]) 

# filtering data on index value 
mask = df.index > 7

print(df[mask])



# importing pandas as pd 
import pandas as pd 
  
# Making data frame from the csv file 
df = pd.read_csv("nba.csv") 
  
# Printing the first 10 rows of  
# the data frame for visualization 
  
#print(df[:10])
#print(df.dropna(inplace = True))

# let's find out the data type of Weight column 
before = type(df.Weight[0]) 

# Now we will convert it into 'int64' type. 
df.Weight = df.Weight.astype('float') 

# let's find out the data type after casting 
after = type(df.Weight[0]) 

# print the value of before 
print(before) 

# print the value of after 
print(after)
print(df['Weight'])


# importing pandas as pd 
import pandas as pd 

# Creating the dataframe 
df = pd.DataFrame({"A":["sofia", 5, 8, 11, 100], 
				"B":[2, 8, 77, 4, 11], 
				"C":["amy", 11, 4, 6, 9]}) 

# Print the dataframe 
print(df) 
print(df.info())

new_df = df[1:]
print(new_df)
print(new_df.info())


# applying infer_objects() function. 
new_df = new_df.infer_objects() 

# Print the dtype after applying the function 
print(new_df.info())


# importing pandas as pd 
import pandas as pd 

# dictionary of lists 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
		'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
		'score':[90, 40, 80, 98]} 

# craeting a dataframe from a dictionary 
df = pd.DataFrame(dict) 

# using iteritems() function to retrieve rows 
for key, value in df.iteritems(): 
	print(key, "\n", value) 
	print()

# importing pandas module 
import pandas as pd 
	
# making data frame from csv file 
#data = pd.read_csv("nba.csv") 

#for i in data.itertuples(): 
#	print(i)


# importing pandas as pd 
import pandas as pd 

# importing numpy as np 
import numpy as np 

# dictionary of lists 
dict = {'First Score':[100, 90, np.nan, 95], 
		'Second Score': [30, 45, 56, np.nan], 
		'Third Score':[np.nan, 40, 80, 98]} 

# creating a dataframe from dictionary 
df = pd.DataFrame(dict) 

# filling a missing value with 
# previous ones 
print(df.fillna(method ='pad'))


# importing pandas as pd 
import pandas as pd 

# importing numpy as np 
import numpy as np 

# dictionary of lists 
dict = {'First Score':[100, 90, np.nan, 95], 
		'Second Score': [30, 45, 56, np.nan], 
		'Third Score':[np.nan, 40, 80, 98]} 

# creating a dataframe from dictionary 
df = pd.DataFrame(dict) 

# filling null value using fillna() function 
print(df.fillna(method ='bfill'))


# importing pandas package 
import pandas as pd 
import numpy as np	
# making data frame from csv file 
data = pd.read_csv("nba_test.csv") 

# Printing the first 10 to 24 rows of 
# the data frame for visualization 
new_data = data[:10]
print(new_data[['Position', 'Number', 'Height']])
#new_data['Position'].fillna("Not Specified", inplace = True)
#print(new_data['Position'])
new_data.replace(to_replace = np.nan, value = "No", inplace =True)
print(new_data[['Position', 'Number', 'Height']])



# importing pandas as pd 
import pandas as pd 
	
# Creating the dataframe 
df = pd.DataFrame({"A":[12, 4, 5, None, 1], 
				"B":[None, 2, 54, 3, None], 
				"C":[20, 16, None, 3, 8], 
				"D":[14, 3, None, None, 6]}) 
	
# Print the dataframe 
print(df)
# to interpolate the missing values 
df.interpolate(method ='linear', limit_direction ='forward', inplace = True) 

print(df)


# importing pandas as pd 
import pandas as pd 

# importing numpy as np 
import numpy as np 

# dictionary of lists 
dict = {'First Score':[100, np.nan, np.nan, 95], 
		'Second Score': [30, np.nan, 45, 56], 
		'Third Score':[52, np.nan, 80, 98], 
		'Fourth Score':[np.nan, np.nan, np.nan, 65]} 

df = pd.DataFrame(dict) 

# using dropna() function	 
print(df.dropna(how = 'all') )








# importing pandas module 
import pandas as pd 
	
# making data frame from csv file 
data = pd.read_csv("nba_test.csv") 
	
# making new data frame with dropped NA values 
new_data = data.dropna(axis = 0, how ='any') 
	
print(new_data)

print("Old data frame length:", len(data)) 
print("New data frame length:", len(new_data)) 
print("Number of rows with at least 1 NA value: ", (len(data)-len(new_data))) 



import numpy as np
arr = np.array(["Hello", "How", "Hi", "Apple", "Ball"])
print("Before sorting: \n", arr)

print("After sorting: \n", np.sort(arr))

lst = ["Hello", "How", "Hi", "Apple", "Ball"]
print(lst)
sortedList = sorted(lst, key = str)
print(sortedList)


# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data)

print(df['Name'])
print(df['Name'].str.lower())


# making data frame from csv file 
data = pd.read_csv("nba.csv") 
   
# converting and overwriting values in column 
data["Team"]= data["Team"].str.upper() 
   
# display 
print(data)


# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Knnuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data) 
    
# dropping null value columns to avoid errors 
df.dropna(inplace = True) 
    
# new data frame with split value columns
df["Address"] = df['Address'].str.split('a', n=1, expand = True)
print(df)


# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[25, 25, 22, 25], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Knnuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data) 
print(df)
filter = df['Age'] == 25
print(df.where(filter).dropna())

# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data) 

new = df['Address'].copy()

df['Name'] = df['Name'].str.cat(new, sep=',')
print(df)


# Define a dictionary containing employee data 
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur junction', 'Kanpur junction', 
                   'Nagpur junction', 'Kannuaj junction'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data)
   
# replacing address name and adding spaces in start and end 
new = df["Address"].replace("Nagpur junction", "  Nagpur junction  ").copy() 
   
# checking with custom string 
print(new.str.strip()==" Nagpur junction")
print(new.str.strip()=="Nagpur junction")
print(new.str.strip()==" Nagpur junction ")


 
# creating a series 
s = pd.Series(['a1', 'b2', 'c3'])
 
# Extracting a data
n= s.str.extract(r'([ab])(\d)')
 
print(n)


# creating a series 
s = pd.Series(['a1', 'b2', 'c3'])
 
# Extracting a data
n = s.str.extract(r'(?P<Geeks>[ab])(?P<For>\d)')
 
print(n)




data = pd.date_range('1/1/2011', periods = 10, freq ='H')
print(data)

import datetime
x = datetime.datetime.now()
print(x.month, x.year)



# Create date and time with dataframe
rng = pd.DataFrame()
rng['Date'] = pd.date_range("01/01/2020", periods = 72, freq = 'H')

# Print the dates in dd-mm-yy format
print(rng.head(5))

 
# Create features for year, month, day, hour, and minute
rng['Year'] = rng['Date'].dt.year
rng['Month'] = rng['Date'].dt.month
rng['Day'] = rng['Date'].dt.day
rng['Hour'] = rng['Date'].dt.hour
rng['Minute'] = rng['Date'].dt.minute


# Print the dates divided into features
print(rng.head(5))



# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
print(df, "\n\n", df1, "\n\n") 


frames = [df, df1]
print(frames)
res1 = pd.concat(frames)
print("\n\n", res1, "\n\n")


# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
 
print(df, "\n\n", df1, "\n\n")


# applying concat with axes
# join = 'inner'
res2 = pd.concat([df, df1], axis=1, join='inner')
 
print(res2, "\n\n")



# using a .concat for
# union of dataframe
res2 = pd.concat([df, df1], axis=1, sort=False)
 
print(res2, "\n\n")



# using join_axes
res3 = pd.concat([df, df1], axis=1, join_axes=[df.index])
 
print(res3, "\n\n")



# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
print(df, "\n\n", df1, "\n\n") 

# using append function
 
res = df.append(df1)
print(res)


# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
    
# Define a dictionary containing employee data 
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[2, 3, 6, 7]) 
  
  
print(df, "\n\n", df1, "\n\n")

# using ignore_index
res = pd.concat([df, df1], ignore_index=True)
 
print(res, "\n\n")


# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Define a dictionary containing employee data 
data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'], 
        'Age':[17, 14, 12, 52], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=[4, 5, 6, 7])
 
print(df, "\n\n", df1, "\n\n")


# using keys 
frames = [df, df1 ]
 
res = pd.concat(frames, keys=['x', 'y'])
print(res, "\n\n")



# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 
   
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=[0, 1, 2, 3])
 
# creating a series
s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')
 
print(df, "\n\n", s1, "\n\n")


# combining series and dataframe
res = pd.concat([df, s1], axis=1)
 
print(res, "\n\n")


# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
# Define a dictionary containing employee data 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2) 
  
 
print(df, "\n\n", df1, "\n\n") 


# using .merge() function
res = pd.merge(df, df1, on='key')
 
print(res, "\n\n")




# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
# Define a dictionary containing employee data 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2) 
  
 
print(df, "\n\n", df1, "\n\n")


# merging dataframe using multiple keys
res1 = pd.merge(df, df1, on=['key', 'key1'])
 
print(res1, "\n\n")


# importing pandas module
import pandas as pd 
 
# Define a dictionary containing employee data 
data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K1', 'K0', 'K1'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],} 
   
# Define a dictionary containing employee data 
data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'key1': ['K0', 'K0', 'K0', 'K0'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']} 
 
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
 
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2) 
  
 
print(df, "\n\n", df1, "\n\n")

# merging dataframe using left keys
res1 = pd.merge(df, df1, how='left', on=['key', 'key1'])
 
print(res1, "\n\n")

# using keys from right frame
res1 = pd.merge(df, df1, how='right', on=['key', 'key1'])
 
print(res1, "\n\n")


# getting union  of keys
res2 = pd.merge(df, df1, how='outer', on=['key', 'key1'])
 
print(res2, "\n\n")

# getting intersection of keys
res3 = pd.merge(df, df1, how='inner', on=['key', 'key1'])
 
print(res3, "\n\n")


# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32]} 
    
# Define a dictionary containing employee data 
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1,index=['K0', 'K1', 'K2', 'K3'])
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
 
 
print(df, "\n\n", df1, "\n\n")


# joining dataframe
res = df.join(df1)
 
print(res, "\n\n")

# getting union
res1 = df.join(df1, how='outer')
 
print(res1, "\n\n")



# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32],
        'Key':['K0', 'K1', 'K2', 'K3']} 
    
# Define a dictionary containing employee data 
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1)
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index=['K0', 'K2', 'K3', 'K4'])
 
 
print(df, "\n\n", df1, "\n\n")

# using on argument in join
res2 = df.join(df1, on='Key')
 
print(res2, "\n\n")



# importing pandas module
import pandas as pd 
  
# Define a dictionary containing employee data 
data1 = {'Name':['Jai', 'Princi', 'Gaurav'], 
        'Age':[27, 24, 22]} 
    
# Define a dictionary containing employee data 
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']} 
  
# Convert the dictionary into DataFrame  
df = pd.DataFrame(data1, index=pd.Index(['K0', 'K1', 'K2'], name='key'))
 
index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                   ('K2', 'Y2'), ('K2', 'Y3')],
                                   names=['key', 'Y'])
  
# Convert the dictionary into DataFrame  
df1 = pd.DataFrame(data2, index= index)
 
 
print(df, "\n\n", df1, "\n\n")


# joining singly indexed with
# multi indexed
result = df.join(df1, how='inner')
 
print(result, "\n\n")



import numpy as np
import pandas as pd

arr = np.array(['h', 'e', 'l', 'l', 'o'])
ser = pd.Series(arr)

print(ser)


lst = ['h', 'e', 'l', 'l', 'o']
ser = pd.Series(lst)
print(ser)


# import pandas and numpy 
import pandas as pd
import numpy as np
 
# creating simple array
data = np.array(['g','e','e','k','s','f', 'o','r','g','e','e','k','s'])
ser = pd.Series(data)
  
  
#retrieve the first element
print(ser[:5])



# importing pandas module  
import pandas as pd  
     
# making data frame  
df = pd.read_csv("nba.csv")  
   
ser = pd.Series(df['Name']) 
data = ser.head(10)
print(data)

print(data[3:6])
print("*******************")
print(data.loc[3:6])

# using .iloc[] function
print(data.iloc[3:6])


# importing pandas module  
import pandas as pd  
 
# creating a series
data = pd.Series([5, 2, 3,7], index=['a', 'b', 'c', 'd'])
 
# creating a series
data1 = pd.Series([1, 6, 4, 9], index=['a', 'b', 'd', 'e'])
 
print(data, "\n\n", data1, "\n\n")
res = data.add(data1, fill_value = 2)
print(res)


# subtracting two series using
# .sub
print(data.sub(data1, fill_value=0))



# Python program converting
# a series into list
 
# importing pandas module  
import pandas as pd  
   
# importing regex module 
import re 
     
# making data frame  
data = pd.read_csv("nba.csv")  
     
# removing null values to avoid errors  
data.dropna(inplace = True)  
   
# storing dtype before operation 
dtype_before = type(data["Salary"]) 
   
# converting to list 
salary_list = data["Salary"].tolist() 
   
# storing dtype after operation 
dtype_after = type(salary_list) 
   
# printing dtype 
print("Data type before converting = {}\nData type after converting = {}"
      .format(dtype_before, dtype_after)) 
   
# displaying list 
print(salary_list)




import pandas as pd 

# a simple dictionary 
dict = {'Geeks' : 10, 
		'for' : 20, 
		'geeks' : 30} 

# create series from dictionary 
ser = pd.Series(dict) 

print(ser) 



import pandas as pd 

import numpy as np 

# giving a scalar value with index 
ser = pd.Series(10, index =[0, 1, 2, 3, 4, 5]) 

print(ser) 


# import pandas and numpy 
import pandas as pd 
import numpy as np 
	
# series with numpy linspace() 
ser1 = pd.Series(np.linspace(3, 33, 3)) 
print(ser1) 
	
# series with numpy linspace() 
ser2 = pd.Series(np.linspace(1, 100, 10)) 
print("\n", ser2) 



# import pandas and numpy 
import pandas as pd 
import numpy as np 

# creating simple array 
data = np.array(['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']) 
ser = pd.Series(data) 


# retrieve the first element 
print(ser[0]) 



# importing pandas and numpy 
import pandas as pd 
import numpy as np 
	
ser = pd.Series(np.arange(3, 9), index =['a', 'b', 'c', 'd', 'e', 'f']) 
	
print(ser[['a', 'd', 'g', 'l']]) 

# Program to Create Data Frame with two dictionaries 
dict1 ={'a':1, 'b':2, 'c':3, 'd':4}	 # Define Dictionary 1 
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2 
Data = {'first':dict1, 'second':dict2} # Define Data with dict1 and dict2 
df = pd.DataFrame(Data) # Create DataFrame
print(df)


# Program to create Dataframe of three series 
import pandas as pd 

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])		 # Define series 1 
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3]) # Define series 2 
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])	 # Define series 3 


Data ={'first':s1, 'second':s2, 'third':s3} # Define Data 
dfseries = pd.DataFrame(Data)			 # Create DataFrame 
print(dfseries)
