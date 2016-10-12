import pickle

data = {'name' : 'Corey',
        'age' : 666,
        'value' : (None, True, False)
        }


file = open('/home/corey/pickle.txt', 'wb')
pickle.dump(data, file)
file.close()

file = open('/home/corey/pickle.txt', 'rb')
pickle_data = pickle.load(file)
file.close()

