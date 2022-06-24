import psycopg2

try:
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "root",
        database = "Lib"
    )
    connection.autocommit = True
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")

    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE users(
            id serial PRIMARY KEY,
            first_name varchar(50) NOT NULL,
            nick_name varchar(50) NOT NULL);""")

    with connection.cursor() as cursor:
        cursor.execute("""INSERT INTO users(first_name, nick_name) VALUES('Sergey', 'REM')""")
        print("[INFO] Insert completed")

    with connection.cursor() as cursor:
        cursor.execute("""SELECT * FROM users""")    
        print(cursor.fetchone())

    with connection.cursor() as cursor:
        cursor.execute("""DROP TABLE users""")
        print("[INFO] Table was deleted")
    
except Exception as _ex:
    print("[INFO] Something goes wrong... *треск сверчков")
finally:
    if connection:
        connection.close()
        print("[INFO] Closed")