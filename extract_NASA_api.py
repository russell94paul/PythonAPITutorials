import requests

# request = requests.get('http://api.open-notify.org')
# print(request.text)

# print the json data as text
people = requests.get('http://api.open-notify.org/astros.json')
print(people.text)

# Converts data to python dictionary format
people_json  = people.json()
print(people_json)


# To print the number of people in space
print("Number of people in space:",people_json['number'])

# To print the names of people in space using a for loop
for p in people_json['people']:
    print(p['name'])
