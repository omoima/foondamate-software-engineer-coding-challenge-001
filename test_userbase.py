import unittest
from urllib import response
import api
import json
from datetime import datetime

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

    def test_filter(self):
        response = api.filter(datetime.strptime('01-01-2022','%d-%m-%Y').date(),datetime.strptime('04-01-2022','%d-%m-%Y').date())
        self.assertTrue(len(response) == 4)

    def test_filter2(self):
        response = api.filter(datetime.strptime('01-01-2022','%d-%m-%Y').date(),datetime.strptime('01-01-2022','%d-%m-%Y').date())
        self.assertTrue(len(response) == 1)

    def test_filterstr(self):
        response = api.filter(datetime.strptime('01-01-2022','%d-%m-%Y').date(),'02-01-2022')
        self.assertTrue(len(response) == 0)

    def test_filterwrong(self):
        response = api.filter(datetime.strptime('01-05-2022','%d-%m-%Y').date(),datetime.strptime('11-05-2022','%d-%m-%Y').date())
        self.assertTrue(len(response) == 0)

if __name__ == '__main__':
    unittest.main()