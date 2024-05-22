import sqlite3
print("hello")
con = sqlite3.connect('temp.db')
cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score)")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
def GetQuery():
    pass

def AddData():
    pass
