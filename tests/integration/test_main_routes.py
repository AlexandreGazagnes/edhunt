import unittest
import pytest

import sys
import os
import logging

# myPath = os.path.dirname(os.path.abspath(__file__))
# print(myPath)
# sys.path.insert(0, myPath + '/../')

from sultan import *
app.testing = True


class TestMainRoutes(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        print('Done')

    def test_home1(self):
        result = self.app.get('/')

    def test_home2(self):
        result = self.app.get('/home')

    def test_about(self):
        result = self.app.get('/about')

    def test_login(self):
        result = self.app.get('/login')

    def test_register(self):
        result = self.app.get('/register')


# @pytest.fixture()
# def give_app():
#     app.testing = True
#     _app = app.test_client()
#     return _app

# class TestMainRoutes():

#     def test_home1(self, give_app):
#         give_app()get('/')

#     def test_home2(self,give_app):
#         give_app()get('/home')

#     def test_about(self, give_app):
#         give_app()get('/about')

#     def test_login(self, give_app):
#         give_app()get('/login')

#     def test_register(self, give_app):
#         give_app()get('/register')


if __name__ == '__main__':
    unittest.main()


# if __name__ == '__main__':
#     myPath = os.path.dirname(os.path.abspath(__file__))
#     logging.info(myPath)
#     sys.path.insert(0, myPath + '/../')
