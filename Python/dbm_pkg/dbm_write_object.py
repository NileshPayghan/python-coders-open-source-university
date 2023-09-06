import dbm


obj = dbm.whichdb('createdb.db')
print(obj)

db = dbm.open('createdb.db', 'n')

db['name'] = 'Nilesh'
db['address'] = 'Pune'
db['pin'] = '431515'

db.close()