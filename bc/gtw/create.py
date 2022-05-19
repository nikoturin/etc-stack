import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="192.168.56.105", port="5432")
print("Database opened successfully")

cur = con.cursor()
cur.execute('''CREATE TABLE STUDENT
      (ADMISSION INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      COURSE        CHAR(50),
      DEPARTMENT        CHAR(50));''')
print("Table created successfully")

con.commit()
con.close()
