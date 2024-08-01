import json

# Json data types
# String
# Number
# Boolean
# Null
# Object
# Array

my_credential = '{"name": "Dexter", "age": 33, "countries": ["FR", "UK"], "cities": {"1": "London"}, "AV": true}'
convert_to_dicts = json.loads(my_credential)
convert_to_json = json.dumps(convert_to_dicts, indent=1, sort_keys=True)

my_dict = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}

# my_file = open('users.json', 'w')
# The dump() method is used when the Python objects have to be stored in a file
# json.dump(my_dict, my_file, indent=4)

# json.load() takes a file object and returns the json objec
my_file = open('users.json')
data = json.load(my_file)

my_file.close()