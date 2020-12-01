# IMPORT SQLITE
import sqlite3

# CONNECT A DB CALLED 'PROCESSES' TO SQLITE (CREATE FILE CALLED PROCESSES.DB)
conn = sqlite3.connect("processes.db")

c = conn.cursor()


# CREATE A DATABASE
c.execute("""CREATE TABLE IF NOT EXISTS processes (
    id integer PRIMARY KEY,
    name text NOT NULL,
    safe integer NOT NULL 
);""")  # id --> integer; name --> text; safe --> integer (boolean - 0/1) 
# SAFE? 0 = NOT SAFE, 1 = SAFE


# METHOD TO ADD PROCESS TO DB IF NEEDED
def addProcess(safeProcessID, safeProcessName, safeProcessBool):
    c.execute("""INSERT INTO processes(id, name, safe) 
                VALUES 
                    (?, ?, ?)""", (safeProcessID, safeProcessName, safeProcessBool))
    conn.commit()

# METHOD TO SEE IF THE PROCESS IS ALREADY IN THE DATABASE : TRUE = EXISTS, FALSE = DOES NOT EXIST
def alreadyExists(processName): 
    c.execute("""SELECT name
                FROM processes
                WHERE name=?""", (processName,))
    result = c.fetchone()
    if result:
        return True
    else:
        return False