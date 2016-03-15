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
            
            try: 

                userinput = raw_input()
                request = userinput.split()[0]
                content = None

                if not len(userinput.split()) < 2: 
                    content = userinput.split(' ',1)[1]

                
                valid_requests = {"help","names","logout","login","msg"}
                if request in valid_requests:
                    print ("This is a valid request")
                    
                    ## Kanskje vi skal utføre bestemte ting her og ikke bare sende data til server.
                    payload = {
                    'request': request,
                    'content': content
                     }

                    print ("Sending payload")
                    self.send_payload(payload)


                else:
                    print ("Not a valid request")    

            except (KeyboardInterrupt):
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
