import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="codebugged"
)
mycursor = mydb.cursor()
#insert
sql = "INSERT INTO employee (name, address) VALUES (%s, %s)"
val = ("Gaurav", "CTO")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#insert multiple
sql = "INSERT INTO employee (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

#Insert one row and return the ID
sql = "INSERT INTO employee (name, address) VALUES (%s, %s)"
val = ("Michelle", "Blue Village")
mycursor.execute(sql, val)
mydb.commit()
print("1 record inserted, ID:", mycursor.lastrowid)

#SELECT and display the table
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Select only name and address
mycursor.execute("SELECT name, address FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Fetchone method - will return the first row of the result
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchone()
print(myresult)

#WHERE
sql = "SELECT * FROM employee WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

