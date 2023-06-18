import mysql.connector
import os



# Establish connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pillow007",
    database="CalHacks"
)

# Create cursor
cursor = conn.cursor()

####REAL
# Execute query
cursor.execute("SELECT videoname FROM metadata WHERE label = 'REAL'")

# Fetch all rows
rows = cursor.fetchall()
dataset_path = 'Detection Algorithm/prepared_dataset/'

# Define the directory and file path
directory_real = 'Detection Algorithm/prepared_dataset/'
file_name = 'real.txt'
file_path = os.path.join(directory_real, file_name)

# Create the directory if it doesn't exist
if not os.path.exists(directory_real):
    os.makedirs(directory_real)

# Open the file in write mode
with open(file_path, 'w') as file:
    # Write the videoname values to the file
    for row in rows:
        file.write(row[0] + '\n')


#####FAKE
# Execute query
cursor.execute("SELECT videoname FROM metadata WHERE label = 'FAKE' LIMIT 16293")

# Fetch all rows
rows = cursor.fetchall()

# Define the directory and file path
directory_fake = 'Detection Algorithm/prepared_dataset/'
file_name_fake = 'fake.txt'
file_path_fake = os.path.join(directory_fake, file_name_fake)

# Create the directory if it doesn't exist
if not os.path.exists(directory_fake):
    os.makedirs(directory_fake)

# Open the file in write mode
with open(file_path_fake, 'w') as file:
    # Write the videoname values to the file
    for row in rows:
        file.write(row[0] + '\n')








# Close cursor and connection
cursor.close()
conn.close()
