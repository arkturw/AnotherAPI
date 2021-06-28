import jsonschema
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from jsonschema import validate
from oauth2 import tokengenerator
import json


app = Flask(__name__)
api = Api(app)


def generate_token(length: int = 40):
    token_generator = tokengenerator.URandomTokenGenerator(length)
    token = token_generator.generate()
    return token


def get_schema(schema_json: str):
    with open(schema_json, 'r') as f:
        _schema = json.load(f)
    return _schema


def get_request(request_json: str):
    with open(request_json, 'r') as f:
        _request = json.load(f)
    return _request


class StartFlow(Resource):

    def get(self):
        return {
            "status": "success",
            "action_token": generate_token()
        }, 200


class PokemonData(Resource):
    # TODO walidacja 'action' i 'action_token'

    current_action_token = ''

    def __init__(self):
        self.current_action_token = generate_token()
        return

    def post(self):
        json_data = request.get_json(force=True)
        schema = get_schema('schema/poke_trainer_schema.json')

        try:
            validate(json_data, schema)
        except jsonschema.exceptions.ValidationError as err:
            print(err)
            err = "Sent request is not valid."
            return {"error": err}, 400
        return {
            "status": "success",
            "action_token": self.current_action_token
        }, 200


api.add_resource(StartFlow, '/start')
api.add_resource(PokemonData, '/pokemon_data')


if __name__ == '__main__':
    app.run(debug=True)

