import json

data = {'name': 'John', 'age': 36, 'info': {'city': 'Toronto'}}

# with open('data.json', 'w') as file:
#     json.dump(data, file)

with open('data.json', 'r') as file:
    read_data = json.load(file)

print(read_data)
