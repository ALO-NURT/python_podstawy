import mysql.connector

database = mysql.connector.connect(
    host="alo-nurt.pl",
    user="alo-uczen",
    password="ALO.mysql9",
    database="alo_test_db"
)

cursor = database.cursor()
cursor.execute('select pesel, first_name, last_name from bank_client')
records = cursor.fetchall()

for record in records:
    print(record)
