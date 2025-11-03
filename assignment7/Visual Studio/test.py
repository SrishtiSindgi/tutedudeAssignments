import psycopg2

def table():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="demo123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE employees (Name TEXT, ID INT, Age INT);''')
    print('Table created successfully')
    conn.commit()
    conn.close()


def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="demo123",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE employees (Name TEXT, ID INT, Age INT);''')
    print('Table created successfully')
    conn.commit()
    conn.close()
