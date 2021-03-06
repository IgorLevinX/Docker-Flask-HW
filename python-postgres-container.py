import os
import time
import psycopg2

os.system(f'docker run -d --name postgres-test -p 5432:5432 -v {os.getcwd()}/db_files:/var/lib/postgresql/data/ -e POSTGRES_HOST_AUTH_METHOD=trust postgres')
time.sleep(5)

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    port="5432",
    database="postgres")

cursor = connection.cursor()
cursor.execute("SELECT current_database()")
result = cursor.fetchall()
print(result)
