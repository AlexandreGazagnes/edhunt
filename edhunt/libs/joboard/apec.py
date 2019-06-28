#!/usr/bin/env python3
# coding: utf-8


from src.misc import *

class Apec(webdriver.Firefox) :

    def __init__(self, user_type) :

        # check args
        assert isinstance(user_type, str)

        # url
        user_type = user_type.lower()
        if user_type == "cadre" :
            url = "https://cadres.apec.fr/home/mon-espace/identification.html"
        elif user_type == "jeune_diplome" :
            url = "https://jd.apec.fr/home/mon-espace/identification.html"
        else  :
            raise AttributeError("user_type need to be specified : cadre, jeune_diplome")

        # driver init
        super().__init__()
        self.get(url)
        self.first_url = url


    def login(self, username, passwd) :

        assert isinstance(username, str)
        assert isinstance(passwd, str)

        self.username = username
        self.password = passwd

        # elements
        _username = self.find_element_by_id("username")
        _passwd = self.find_element_by_id("password")

        _username.send_keys(username)
        _passwd.send_keys(passwd)

        self.find_element_by_id("login.submit.label").click()

        if "loginError" in self.current_url :
            raise AttributeError("username or passwd do not match")

    @property
    def html(self) :
        return self.page_source


    @html.setter
    def html(self, arg) :
        raise ValueError("no autorised to change html")
