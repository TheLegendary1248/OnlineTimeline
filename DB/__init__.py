"""The DB of OnlineTimeline"""
import sqlite3
import threading
def initDB():
    return sqlite3.connect('db.sqlite3')
def RunSQL(db: sqlite3.Connection, query):
    cursor = db.cursor()
    return cursor.execute(db, query)

def load():
    db = initDB()
    return None #change this to a database object
