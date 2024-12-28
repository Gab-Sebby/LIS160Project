import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = '101406'

	)

#1: Preparing a cursor object
cursor0bject = dataBase.cursor()

#2: Create a database
cursor0bject.execute("CREATE DATABASE elderco")

print("All Done!")