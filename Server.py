# -*- coding: utf-8 -*-
import SocketServer
import json
import re
import datetime
import time
"""
Variables and functions that must be used by all the ClientHandler objects
must be written here (e.g. a dictionary for connected clients)
"""

connectedClients = dict{}

userNames = []

class ClientHandler(SocketServer.BaseRequestHandler):
    """
    This is the ClientHandler class. Every time a new client connects to the
    server, a new ClientHandler object will be created. This class represents
    only connected clients, and not the server itself. If you want to write
    logic for the server, you must write it outside this class
    """

    def returnTimeStamp(self):
        ts = time.time()
        return datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')


    response_payload = {
			'timestamp': returnTimeStamp(),
			'sender': 'server',
			'response': None,
			'content': None,
		}

    def handle_userName(self):

        if not re.match("^[A-Za-z0-9]+$", username):


        for conn in connectedClients:



    def handle(self):
        """
        This method handles the connection between a client and the server.
        """
        self.username = None
        self.ip = self.client_address[0]
        self.port = self.client_address[1]
        self.connection = self.request

        # Loop that listens for messages from the client
        while True:
            received_string = self.connection.recv(4096)
            try:
                payload = json.loads(received_string)
                request = payload.get("request")
                content  = payload.get("content")


            except:


            # TODO: Add handling of received payload from client


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    This class is present so that each client connected will be ran as a own
    thread. In that way, all clients will be served by the server.

    No alterations are necessary
    """
    allow_reuse_address = True

if __name__ == "__main__":
    """
    This is the main method and is executed when you type "python Server.py"
    in your terminal.

    No alterations are necessary
    """
    HOST, PORT = 'localhost', 9998
    print 'Server running...'

    # Set up and initiate the TCP server
    server = ThreadedTCPServer((HOST, PORT), ClientHandler)
    server.serve_forever()
