import sqlite3

conn = sqlite3.connect('Members of DURAN.db')
var1 = "histos"
var2 = "histos2"
var3 = "histos3"
var4 = "histos4"
var5 = "DURAN"
c = conn.cursor()

#c.execute("INSERT INTO Registered_members_DURAN VALUES (?, ?, ?, ?, ?)", (var1, var2, var3, var4, var5))

conn.commit()

c.execute("SELECT * FROM Registered_members_DURAN WHERE locating_var='hi5'")

user_list = c.fetchall()

x = 0
for i in user_list:
    if i[3] == "histdsds4":
        x = x + 1
    else:
        pass
if x == 1:
    print("Username already taken")
else:
    print("You are now registered")


conn.commit()

conn.close()