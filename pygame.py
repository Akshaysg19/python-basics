import mysql.connector

mydb = mysql.connector.connect(host='localhost', user='root', password='root', database='world')
mycursor = mydb.cursor()
#mycursor.execute('select * from city')
mycursor.execute('select Name, CountryCode from city')
myresult = mycursor.fetchall()

for x in myresult:
  print(x)