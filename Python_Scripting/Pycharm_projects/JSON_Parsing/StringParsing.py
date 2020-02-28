import json

# with open("01_ProgramHeader.json") as json_file:
#     data = json.load(json_file)

#
# with open("sample.json") as json_file:
#     data = json.load(json_file)

str = """{
  "People":[
	  		{
			  "name": "John",
			  "age": 30,
			  "married": true,
			  "children": ["Ann","Billy"],
			  "pets": null,
			  "cars": [
				{"model": "BMW 230", "mpg": 27.5},
				{"model": "Ford Edge", "mpg": 24.1}]
			  },
			  {  
			  "name": "Smith",
			  "age": 32,
			  "married": true,
			  "children": ["Hillary"],
			  "pets": null,
			  "cars": [
				{"model": "Audi A8", "mpg": 24.5},
				{"model": "Benz", "mpg": 22.1}]
			  }
			]
}


"""
data = json.loads(str)
print(type(data))
print(data)

print(type(data['People']))

for person in data['People']:
    del person['pets']

new_str = json.dumps(data, indent=2, sort_keys=True)

print(new_str)