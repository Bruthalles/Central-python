import dataset

db = dataset.connect('sqlite:///:memory:')

table = db['sometable']
table.insert(dict(name='john doe',age=37))
table.insert(dict(name='jane ',age=34, gender='female'))

john = table.find_one(name='john doe')