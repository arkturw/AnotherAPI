from jsonschema import validate
import json

# file = open('schema.json')
# schema = json.load(file)
# file = open('request.json')
# data = json.load(file)
# file.close()
#
# validate(data, schema)


def get_schema(schema_json: str):
    with open(schema_json, 'r') as f:
        _schema = json.load(f)
    return _schema


def get_request(request_json: str):
    with open(request_json, 'r') as f:
        _request = json.load(f)
    return _request


schema = get_schema('poke/poke_trainer_schema.json')
data = get_request('poke/poke_trainer_request.json')

validate(data, schema)
