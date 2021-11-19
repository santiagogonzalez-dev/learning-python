import sqlite3

def createDB():
    conn = sqlite3.connect('testing.db')
    conn.commit()
    conn.close()

def createTable():
    conn = sqlite3.connect('testing.db')
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE usuarios (
            username text,
            edad integer
        )"""
    )
    conn.commit()
    conn.close()

def insertRow(username, edad):
    conn = sqlite3.connect('testing.db')
    cursor = conn.cursor()
    instruccion = f"INSERT INTO usuarios VALUES ('{username}', {edad})"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

def showContent():
    conn = sqlite3.connect('testing.db')
    cursor = conn.cursor()
    instruccion = f"SELECT * FROM usuarios"
    cursor.execute(instruccion)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    testingtest = showContent()
    print(testingtest)
    # createDB()
    # createTable()
    # insertRow('santigotest', 20)
    # insertRow('testing', 33)
