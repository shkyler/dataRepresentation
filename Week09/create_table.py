import mysql.connector
mydb=mysql.connector.connect(
  host="localhost",
  user="root",password="root",
  database="datarepresentation")
mycursor=mydb.cursor()
sql="CREATE TABLE student(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255))"
mycursor.execute(sql)