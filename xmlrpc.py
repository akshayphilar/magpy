__author__ = 'akshayphilar'
from xmlrpclib import ServerProxy


class XMLRPC(object):

    def __init__(self, url, apiuser, apikey):
        self.url = url
        self. apiuser = apiuser
        self.apikey = apikey
        self.session = None
        self.client = None

    def connect(self):
        self.client = ServerProxy(self.url)

    def __enter__(self):
        if self.client is None:
            self.connect()

        self.session = self.client.login(self.apiuser, self.apikey)

    def __exit__(self):
        self.client.endSession(self.session)

    def call(self, resource_path, arguments):
        return self.client.call(self.session, resource_path, arguments)

    def multiCall(self, calls):
        return self.client.multiCall(self.session, calls)
