import numpy
import tensorflow
import mysql.connector

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Pillow007',
    database='Local instance 3306'
)

cursor = connection.cursor();

