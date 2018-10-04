#!/usr/bin/python
'''
#Create
c.execute(\'''CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);\''')
#INSERT
c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )");
#SELECT
cursor = c.execute("SELECT id, name, address, salary  from COMPANY") return a tuple
for row in cursor:
    print row
#UPDATE
c.execute("UPDATE COMPANY set SALARY = 25000.00 where ID=1")
#DELETE
c.execute("DELETE from COMPANY where ID=2;")

conn.commit() # only commit,it can hava a difference
conn.close()
c.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name") query the form name
'''

import  sqlite3
conn = sqlite3.connect('course.db')
c = conn.cursor() #get a handle of test db
print "Opened database successfully"
cursor = c.execute("SELECT * \
                FROM Apply A")
c.execute(".mode column")
#query
for row in cursor:
    print row
