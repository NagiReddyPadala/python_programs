import json


with open('sample.json') as f:
    data = json.load(f)

for person in data['People']:
    print(person)
    print(person['name'])
    print(person['cars'][0]['model'])
    del person['pets']

with open('new_sample.json', 'w') as f:
    json.dump(data, f, indent=2)