import unittest
from .backend_client import BackendClient
import os
import configparser

class BackendSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        conf = cls.readConfig()
        cls.client = BackendClient(conf['backend']['host'], conf['backend']['key'])

    @staticmethod
    def readConfig():
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        config_file = __location__ + '/' + 'config.ini'
        cp  = configparser.ConfigParser()
        cp.read(config_file)

        return cp


    # @staticmethod
    # def assertDictContainsSubset(self, subset, dictionary, msg=None):