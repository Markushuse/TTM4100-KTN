# -*- coding: utf-8 -*-
import socket
import json
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """
        self.serverport = server_port
        self.h = host
        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.MParser = MessageParser()
        self.MReceiver = MessageReceiver(self, self.connection)
        self.run()


    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.h, self.serverport))
        self.MReceiver.start()

        while True:
            userInput = raw_input()
            try:
                if userInput:
                    request, content = userInput.split()
                    if not content:
                        content = None
                payload = {
                    'request': request,
                    'content': content
                }
                self.send_payload(payload)

            except KeyboardInterrupt:
                self.disconnect()

    def handleInput(self, userInput):
        message = userInput.split(' ')

    def disconnect(self):
        self.connection.close()
        print "Server disconnected."


    def receive_message(self, message):
        print self.MParser.parse(message)

    def send_payload(self, data):
        payload = json.dumps(data)
        self.connection.send(payload)


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)