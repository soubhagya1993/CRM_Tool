import mysql.connector

database = mysql.connector.connect(host='localhost',user='root',passwd ='root')


# prepare cusrsor object
cursorObeject = database.cursor()

# create a database
cursorObeject.execute("CREATE DATABASE crmdb_new")

print("Done")
