from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        port="3306",
        user="testing-user",
        password="testing-password",
        database="Employees",
        # Employees is the database, Employee is the table
    ) as connection:
        print(connection)
        cursor = connection.cursor()
        cursor.execute('DESCRIBE Employee')
        table = cursor.fetchall()
        print(table)

        cursor.execute('SELECT * FROM Employee')
        second_table = cursor.fetchall()
        print(second_table)
except Error as e:
    print(e)
