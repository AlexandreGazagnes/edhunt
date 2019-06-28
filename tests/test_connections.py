#!/usr/bin/env python3
# coding: utf-8

import sys, os
import pytest

try :
    myPath = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, myPath + '/../')
except :
    sys.path.insert(0, "/home/alex/sultan")

from src import *


class TestApecConnection():

    def test_init_fails(self):

        with pytest.raises(TypeError) :
            a = Apec()

        for i in [3, None, list()] :
            with pytest.raises(AssertionError):
                a = Apec(i)


        with pytest.raises(AttributeError):
                a = Apec("a")

    def test_init_success(self):

        apec = Apec("cadre")
        apec.close()

        apec = Apec("jeune_diplome")
        apec.close()

    def test_login_fails(self) :

        apec = Apec("cadre")

        with pytest.raises(TypeError) :
            apec.login("a")

        with pytest.raises(TypeError) :
            apec.login()

        with pytest.raises(AssertionError) :
            apec.login(None, "a")

        with pytest.raises(AssertionError) :
            apec.login("a", None)

        with pytest.raises(AttributeError) :
            apec.login('a', 'a')


    def test_login_success(self) :

        apec = Apec("cadre")
