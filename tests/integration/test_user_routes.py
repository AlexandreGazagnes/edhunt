import unittest
import sys
import os
import logging
import json
import time


from sultan import *
app.testing = True


DATA = {'email': 'admin@admin.fr', 'password': 'azertyui'}


class TestMainRoutes(unittest.TestCase):

    def tearDown(self):
        print('Done')

    def test_connection_success(self):
        with app.test_client() as client:
            result = client.post('/login',
                                 data=DATA)
            result = client.get("/manage_user")
            time.sleep(3)
            print(result.data.decode("utf8"))

    def test_connection_fail(self):
        with app.test_client() as client:
            result = client.post('/login',
                                 data={})
            result = client.get("/manage_user")
            time.sleep(3)
            print(result.data.decode("utf8"))


if __name__ == '__main__':
    unittest.main()
