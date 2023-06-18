import mysql.connector

# Establish connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pillow007",
    database="CalHacks"
)

# Create cursor
cursor = conn.cursor()

# Execute query
cursor.execute("SELECT * FROM metadata")

# Fetch all rows
rows = cursor.fetchall()

# Process the dataset
for row in rows:
    print(row)

# Close cursor and connection
cursor.close()
conn.close()
