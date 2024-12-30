import mysql.connector.python

dataBase = mysql.connector.python.connect(
	host = 'localhost',
	user = 'root',
	passwd = '101406'

	)

#1: Preparing a cursor object
cursorObject = dataBase.cursor()

#2: Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")