import unittest
from urllib import response
import api
import json

class Test_Userbase(unittest.TestCase):

    def test_code(self):
        response = api.get_userbase()
        self.assertEqual(response.status_code, 200)

    def test_notnull(self):
        response = api.get_userbase()
        self.assertNotEqual(response.text, '')

    def test_jsontype(self):
        response = api.get_userbase()
        self.assertTrue(json.loads(response.text))

    def test_list(self):
        response = api.userbase_list()
        self.assertEqual(type([]), type(response))

    def test_notempty(self):
        response = api.userbase_list()
        self.assertTrue(len(response) > 0)

if __name__ == '__main__':
    unittest.main()