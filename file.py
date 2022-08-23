import sqlite3
#Creating Connection and Database
conn = sqlite3.connect('pfsd2.db')
print("Opened database successfully")
#Creating a table
conn.execute('''CREATE TABLE sqlitexample
        (ID number,name text,mark1 number)''')
print("Table created successfully")
#Inserting a data into the table
conn.execute("Insert into sqlitexample values (2100030958, 'BODAPATI SUJITHA',50)")
print("Inserted Successfully")
#Cursor - It is an object that is used to make the
# connection for executing SQL queries.
# It acts as middleware between
# SQLite database connection and SQL query
#Creating Cursor
cur = conn.cursor()
#Retrieve Data from Database and print
for row in cur.execute('SELECT * FROM sqlitexample'):
   print(row)
data1 = [(2100030973,'RAJESH',50),
        (2100031072,'SRI LAKSHMI',44)
        (2100031231,'BALAJI',43)
        (2100031316,'KEERTHANA',10)
        ]
#Inserting Multiple data into the table
cur.executemany('INSERT INTO sqlitexample VALUES(?,?,?);',data1);
print("Inserted Multiple data Successfully")
for row in cur.execute('SELECT * FROM sqlitexample'):
   print(row)
#Update a Specific data in table
cur.execute("UPDATE sqlitexample SET name='Deepak' where name = 'NIKHIL SAI'")
print("Updated Successfully")
#Retrieve Data from Database and print
for row in cur.execute('SELECT * FROM sqlitexample'):
   print(row)
#Deleting Specific rows from table
cur.execute("DELETE from sqlitexample where ID = 2000030140 ")
print("Deleted a specific rows from table")
for row in cur.execute('SELECT * FROM sqlitexample'):
   print(row)
#Deleting All rows from table
cur.execute('DELETE FROM sqlitexample',);
print('We have deleted', cur.rowcount, 'records from the table.')
# Save (commit) the changes
conn.commit()
#Close the Connection
conn.close()