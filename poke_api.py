import random

import jsonschema
from flask import Flask, jsonify, request, session
from flask_restful import Resource, Api, reqparse
from jsonschema import validate
import json


app = Flask(__name__)
app.secret_key = 'demoapi123456!@#$%^'
api = Api(app)


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
        session['name'] = str(random.randint(1000, 9999))
        print(session['name'])
        return {
            "status": "success",
            "next_step": "POKEMON_DATA"
        }, 200


class PokemonData(Resource):
    # TODO walidacja 'action' i 'action_token'

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
            "next_step": "DALEJ_NIE_WIEM"
        }, 200


api.add_resource(StartFlow, '/start')
api.add_resource(PokemonData, '/pokemon_data')


if __name__ == '__main__':
    app.run(debug=True)

