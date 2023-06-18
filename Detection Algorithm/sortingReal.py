import mysql.connector
import os
import random


# Establish connection
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Pillow007",
    database="CalHacks"
)

# Create cursor
cursor = conn.cursor()

#####REAL
# Execute query
cursor.execute("SELECT videoname FROM metadata WHERE label = 'REAL' LIMIT 100")

# Fetch all rows
rows = cursor.fetchall()

# Shuffle the rows randomly
random.shuffle(rows)

# Split the rows into two groups
training_rows = rows[:70]
validation_rows = rows[70:]

# Define the directory paths
training_directory = 'Detection Algorithm/training/real'
validation_directory = 'Detection Algorithm/validation/real'

# Create the directories if they don't exist
if not os.path.exists(training_directory):
    os.makedirs(training_directory)
if not os.path.exists(validation_directory):
    os.makedirs(validation_directory)

# Define the file paths
training_file_path = os.path.join(training_directory, 'real.txt')
validation_file_path = os.path.join(validation_directory, 'real.txt')

# Open the training file in write mode
with open(training_file_path, 'w') as training_file:
    # Write the videoname values to the training file
    for row in training_rows:
        training_file.write(row[0] + '\n')

# Open the validation file in write mode
with open(validation_file_path, 'w') as validation_file:
    # Write the videoname values to the validation file
    for row in validation_rows:
        validation_file.write(row[0] + '\n')








# Close cursor and connection
cursor.close()
conn.close()