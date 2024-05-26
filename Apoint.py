import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='cars24@123',database='Bike_part')
mycursor=mydb.cursor()
mycursor.execute("create table part(name varchar(50),garde varchar(20),price int,id int)") 