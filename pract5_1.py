import pickle

data = {'login': 'fdghfg', 'password': 'dfgdf1112'}
serialized_data = pickle.dumps(data)
print(serialized_data)
print(pickle.loads(serialized_data))

