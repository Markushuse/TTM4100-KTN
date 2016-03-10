import json

class MessageParser():
    def __init__(self):

        self.possible_responses = {
            'error': self.parse_error,
            'info': self.parse_info,
            'message': self.parse_message,
            'history': self.parse_history,
            'help': self.parse_help
	    # More key:values pairs are needed
        }

    def parse(self, payload):
        payload = json.loads(payload)
        if payload['response'] in self.possible_responses:
            return self.possible_responses[payload['response']](payload)
        else:
            # Response not valid

    def parse_error(self, payload):

    def parse_info(self, payload):

    def parse_message(self, payload):

    def parse_history(self, payload):

    def parse_help(self, payload):

    # Include more methods for handling the different responses...
