import csv
import sqlite3

INSERT_CMD_STUB = "INSERT INTO "
VALUES_CMD_STUB = "VALUES "

dbEntriesToAppend = []

tarDb = "C:\\Users\\benja_000\\Documents\\Hack24\\Holding-out-for-a-hero\\data\\ControlRoom_test.db"#input("db to populate:")
tarFile = input("File to include:")
tarTable = input("Which table are these entries being appended to?")

try:
    #INITIALISE DATABASE
    dbConnection = sqlite3.connect(tarDb)
    dbConnection.isolation_level = "DEFERRED"
    dbCursor = dbConnection.cursor()

    dbCursor.execute(".tables")
    print(dbCursor.fetchall())

    print("Hello")

    #OPEN CSV
    dataRead = csv.reader(open(tarFile, newline=''), delimiter=',')#, quitechar=',')
    next(dataRead)
    for row in dataRead:
        dbEntriesToAppend.append(row)

    print (dbEntriesToAppend)
    dataRead.close()

except:
    print("FAIL")
#    dbConnection.close()
    #dataRead.close()