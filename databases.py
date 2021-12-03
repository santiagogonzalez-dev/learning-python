import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysqlserver',
    database='mytestingdatabase',
)

cursor = midb.cursor()

cursor.execute('SELECT * FROM mytestingtable')

resultado = cursor.fetchall()

print(resultado)
