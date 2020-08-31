import requests

# Datamuse is an API for find words that rhyme with eachother

# Create dictionary to store any parameters being passed to the endpoint
parameter = {"rel_rhy":"ninth"}
request = requests.get('https://api.datamuse.com/words',parameter)

# Converting to dictionary and printing the first 3 elements in the dictionary
rhyme_json = request.json()
for i in rhyme_json[0:3]:
 print(i['word'])
