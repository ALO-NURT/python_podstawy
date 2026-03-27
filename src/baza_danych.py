import mysql.connector


database = mysql.connector.connect(
    host="alo-nurt.pl",
    user="",
    password="",
    database="alo_test_db"
)

cursor = database.cursor()
cursor.execute('select * fron bank_client')
records = cursor .fetchall()

for record in records:
    print(record)
