from initdata import bob,sue
import shelve
db = shelve.open('people-shelve.txt')
db['bob'] = bob
db['sue'] = sue
db.close()