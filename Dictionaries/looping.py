user = {
    'name': 'derrick',
    'email': 'derrick@gmail.com',
    'age': '20'
}

# Looping through key,value pairs

for key, value in user.items():
    print('\nKey: ' + key)
    print('Value: ' + value)

# Looping through keys
for details in user.keys():
    print(details)

# Looping through values
for value in user.values():
    print(value)
