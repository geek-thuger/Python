import shelve
db = shelve.open('people-shelve.txt')
for key in db:
    print(key,'=>\n',db[key])
print(db['sue']['name'])
db.close()