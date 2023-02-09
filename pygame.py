import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='world')
mycursor = mydb.cursor()
#mycursor.execute('select * from city')
#mycursor.execute('select Name, CountryCode from city')
#mycursor.execute('select * from city order by CountryCode')
mycursor.execute('select * from city order by CountryCode desc')
myresult = mycursor.fetchall()

for x in myresult:
  print(x)