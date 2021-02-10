import sqlite3

conn = sqlite3.connect('Members of DURAN.db')

c = conn.cursor()


c.execute("SELECT * FROM Registered_members_DURAN WHERE locating_var='DURAN'")

user_list = c.fetchall()

for i in user_list:
    print("Namn: " + i[1] + ", Användarnamn: " + i[2] + ")")

conn.commit()

conn.close()