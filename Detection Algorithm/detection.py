import numpy
import tensorflow
import mysql.connector

connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Pillow007',
    database='Local instance 3306'
)

cursor = connection.cursor();
