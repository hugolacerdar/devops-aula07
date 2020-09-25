import sqlite3

conn = sqlite3.connect("exercicio2.db")

c = conn.cursor()

c.execute('''CREATE TABLE ex2
(id real PRIMARY KEY, nome text NOT NULL, email text)''')

c.execute('''INSERT INTO ex2
VALUES (1, 'Hugo', NULL)''')

conn.commit()

conn.close()