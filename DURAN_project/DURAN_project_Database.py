import sqlite3

conn = sqlite3.connect('Members of DURAN.db')

c = conn.cursor()


# Opens Database
c.execute("""CREATE TABLE Registered_members_DURAN (
            social_security_number text UNIQUE,
            name text,
            username text UNIQUE,
            password text,
            locating_var text
            )""")


conn.commit()

conn.close()