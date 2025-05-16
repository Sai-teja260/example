import mysql.connector

db = mysql.connector.connect(
    host="0.0.0.0",
    user="saiteja",
    password="Saiteja@143",
    database="mydatabase"
)

cursor = db.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255)
    )
""")

sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
values = ("Alice", "alice@example.com")
cursor.execute(sql, values)

db.commit()

print("Data inserted successfully!")

cursor.close()
db.close()