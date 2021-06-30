from oauth2 import tokengenerator
import base64
import json
import datetime
from encodings import utf_8


def generate_token(expected_action: str):
    date = str(datetime.datetime.now())
    data = {
        'date': date,
        'action': expected_action
    }
    data = json.dumps(data)
    data = bytes(data, encoding='utf-8')
    data = base64.b64encode(data)
    print(data)
    # test
    data = base64.b64decode(data)
    data = json.loads(data)
    print(data)
    # ====
    return data


# def check_token(expected_action: str):
#     date = str(datetime.datetime.now())
#     data = {
#         'date': date,
#         'action': expected_action
#     }
#     data = json.dumps(data)
#     print(data)
#     return data


class ActionToken:

    def __init__(self):
        self.token_generator = tokengenerator.URandomTokenGenerator(length=40)
        self.old_value = None
        self.new_value = None
        return

    def get_action_token(self):
        # print('get_action_token')
        # print(self.value)
        return self.old_value

    def generate_action_token(self):
        self.value = self.token_generator.generate()
        # print('generate_action_token')
        # print(self.value)
        return


token = generate_token('test')

# at = ActionToken()
# at.get_action_token()
# at.generate_action_token()
# at.get_action_token()