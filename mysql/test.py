import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="MySql@123"
)

print(mydb)