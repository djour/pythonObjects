"""
Created on Sat Jun 6 

@author: koeifans
"""

import unittest
from main import User
from superuser import SuperUser

class TestStringMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.user = User("John", "password", "john@some.come", "12/25/1999")
        self.superuser = SuperUser('jon', 'password', 'jon@some.com', '12/24/1999', 'admin')

    def tearDown(self):
        print('tearDown\n')

    def test_username(self):
        self.assertEqual(self.user._username, 'John')
        self.assertEqual(self.superuser._username, 'jon')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()