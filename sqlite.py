# IMPORT SQLITE
import sqlite3

# CONNECT A DB CALLED 'PROCESSES' TO SQLITE (CREATE FILE CALLED PROCESSES.DB)
conn = sqlite3.connect("processes.db")

c = conn.cursor()


# CREATE A DATABASE
c.execute("""CREATE TABLE processes (
    id integer PRIMARY KEY,
    name text NOT NULL,
    safe integer NOT NULL 
);""")  # id --> integer; name --> text; safe --> integer (boolean - 0/1)


# METHOD TO ADD PROCESS TO DB IF NEEDED
def addProcess(safeProcessID, safeProcessName, safeProcessBool):
    c.execute("INSERT INTO processes VALUES (safeProcessID, safeProcessName, safeProcessBool);")
    conn.commit()

# CLOSE CONNECTION
conn.close()