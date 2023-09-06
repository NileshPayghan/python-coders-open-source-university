import dbm

db = dbm.open('createdb.db', 'r')

k = db.firstkey()
while k!= None:
    print(k)
    k = db.nextkey(k)
