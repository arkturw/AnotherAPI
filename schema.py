from jsonschema import validate
import json

file = open('schema.json')
schema = json.load(file)
file = open('request.json')
data = json.load(file)
file.close()

validate(data, schema)

