import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,
            'help': self.parse_help
        }

    def parse(self, payload):
        payload = json.loads(payload)
        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            print 'Response not valid.'

    def parse_error(self, payload):
        return '[{}] Error: {}'.format(payload['timestamp'], payload ['content'])

    def parse_info(self, payload):
         return '[{}] Info: {}'.format(payload['timestamp'], payload ['content'])

    def parse_message(self, payload):
         return '[{}] Message: {}'.format(payload['timestamp'], payload ['content'])

    def parse_history(self, payload):
        history = {}
        in history ['content']:
        str = ""
        for payload in history ['content']:
            payload = json.loads(payload)
            str += "\n".format(self.parse_message(payload))

    def parse_help(self, payload):
         return '[{}] Help: {}'.format(payload['timestamp'], payload ['content'])
