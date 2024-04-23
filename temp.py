import pickle, gzip

with open('person.pickle', 'rb') as file:
    read_person = pickle.load(file)

print((type(read_person)), read_person)
# read_person.print_info()