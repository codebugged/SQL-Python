import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="codebugged"
)
mycursor = mydb.cursor()
#create a table
mycursor.execute("CREATE TABLE employee (name VARCHAR(255), address VARCHAR(255))")
#check if table exists
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)