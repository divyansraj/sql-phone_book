import sqlite3

conn = sqlite3.connect('phonebook.db')
c = conn.cursor()

c.execute('''DROP TABLE IF EXISTS CONTACTS''')

c.execute('''CREATE TABLE CONTACTS
             (ID INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Cell TEXT, Email TEXT)''')

contacts_data = [
    ('AMIT KUMAR', '+91 1231231232', 'amit@example.com'),
    ('AMISHA PATEL', '+91 1234554321', 'amisha@example.com'),
    ('DEEPAK KUMAR', '+91 0989098890', 'deepak@example.com'),
    ('MANISHA', '+91 6566789980', 'manisha@gmail.com'),
    ('HImanshu', '+91 5555555555', 'raj@gmail.com')
]

c.executemany('INSERT INTO CONTACTS (Name, Cell, Email) VALUES (?, ?, ?)', contacts_data)

conn.commit()

c.execute('SELECT * FROM CONTACTS')
all_contacts = c.fetchall()
for contact in all_contacts:
    print(contact)

conn.close()
