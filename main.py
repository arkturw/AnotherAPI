from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
from oauth2 import tokengenerator
from random import choice
import string


app = Flask(__name__)
api = Api(app)


class Test(Resource):

    user_data = {
        'username': 'jan_nowak',
    }
    current_action_token = ''

    def __init__(self):
        self.current_action_token = self.generate_token()
        return

    def generate_token(self, length: int = 40):
        token_generator = tokengenerator.URandomTokenGenerator(length)
        token = token_generator.generate()
        return token

    def get_current_action_token(self):
        return self.current_action_token

    def get(self):
        self.user_data['password'] = self.generate_token(10)
        self.current_action_token = self.generate_token()
        response = jsonify(
            user_data=self.user_data,
            action_token=self.current_action_token
        )
        response.status_code = 200
        return response

    def post(self):
        json_data = request.get_json(force=True)
        un = json_data['username']
        pw = json_data['password']

        if un == self.user_data['username']:
            if pw == self.user_data['password']:
                #     return jsonify(u=un, p=pw)
                return {
                           'status': "success",
                           'action_token': self.get_current_action_token()
                       }, 200
            else:
                return {
                           'error': 'User unauthorized.'
                       }, 403
        else:
            return {
                       'error': f"'{un}' user not found."
                   }, 404


api.add_resource(Test, '/test')


if __name__ == '__main__':
    app.run(debug=True)

