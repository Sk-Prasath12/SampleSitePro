import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Sri@2011'
)

print(db)

#cursor 
mycursor=db.cursor()















































