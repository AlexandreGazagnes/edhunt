from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from pyvirtualdisplay import Display

from edhunt import warning, info
from time import sleep
from edhunt.config import Params


from bs4 import BeautifulSoup


SLEEP = 0.5


class Apec(webdriver.Firefox):

    url_jd = "https://jd.apec.fr/home/mon-espace/identification.html"
    url_cadre = "https://cadres.apec.fr/home/mon-espace/identification.html"

    def __init__(self, status='cadre'):
        """init method"""

        url = self.url_cadre if (status == "cadre") else self.url_jd
        try:
            super().__init__()
        except:
            super().__init__(executable_path='edhunt/plateforms/webdriver/geckodriver')

        self.status = status
        self.first_url = url
        self.connected = False
        self.errors = []
        self.email = None
        self.password = None
        self.page_nb = 0
        sleep(SLEEP)
        warning("apec reached")

    def login(self, email, password, status=None):

        self.email = email
        self.password = password

        if status:
            self.status = status
        url = self.url_cadre if (self.status == "cadre") else self.url_jd

        self.get(url)
        sleep(SLEEP)
        _username = self.find_element_by_id("username")
        _passwd = self.find_element_by_id("password")
        _username.send_keys(email)
        sleep(SLEEP)
        _passwd.send_keys(password)
        sleep(SLEEP)
        self.find_element_by_id("login.submit.label").click()
        sleep(SLEEP)
        if "Error" in self.current_url:
            self.connected = False
            self.errors.append("Login ou mot de passe incorrect ")
        else:
            self.connected = True

    def test_connexion(self, email, password, status=None):

        if status:
            self.status = status
        second_status = "jd" if (self.status == "cadre") else "cadre"

        self.login(email, password, status)
        if self.connected:
            return (True, "You did it for cadre!", "success")

        self.login(email, password, second_status)
        if self.connected:
            return (True, "You did it for jd !", "success")

        return (False, self.errors, "danger")

    def perform_search_light(self, words, loc):

        # connexion
        if not self.connected:
            raise AttributeError("Not connected")

        # get if needed
        url = "https://cadres.apec.fr/home.html"
        if self.current_url != url:
            self.get(url)
            sleep(SLEEP * 3)

        # perform the search_lig
        _words = self.find_element_by_id("keywords")
        _loc = self.find_element_by_class_name("lieuautocomplete")
        _words.send_keys(words)
        sleep(SLEEP)
        _loc.send_keys(loc)
        sleep(SLEEP * 3)
        _loc.send_keys(Keys.TAB)
        sleep(SLEEP)
        self.find_element_by_class_name("btn-block").click()

        sleep(SLEEP)

        if ("mes-offres" in self.current_url) and ("recherche-des-offres-demploi" in self.current_url):
            pass
        else:
            raise AttributeError("apec do not reach the results page")

        warning("SEARCH DONE")

        return True, "search_done", "info"

    def scrap_search_light(self):
        sleep(SLEEP * 2)
        soup = BeautifulSoup(self.page_source)
        _soup = soup.find_all("div", attrs={"class": "offre ng-scope"})

        if len(_soup) == 0:
            return []

        jobs_list = list()
        for _s in _soup:
            try:
                job = dict()
                job["company"] = _s.find("span", attrs={"bo-text": "offre.enseigne"}).text
                job["job"] = _s.find("span", attrs={"bo-text": "offre.intitule"}).text
                job["plateform"] = "apec"
                job["url"] = _s.find("a")["href"]
                job["loc"] = _s.find("span", attrs={"bo-text": "offre.lieux[0].libelleLieu"}).text
                job["applied"] = False
                job["send"] = False
                job["text"] = _s.find("p", attrs={"class": "detail"}).text
                job["created"] = _s.find("span", attrs={"bo-text": "offre.datePublication | date:'shortDate'"}).text
                _rem = _s.find("span", attrs={"ng-bind": "ro.getSalaireTexteDisplay(offre)"}).text.replace("|", "")
                job["rem"] = _rem if _rem else "-"
                _contract = _s.find("span", attrs={"ng-bind": "ro.getTypeContratDisplay(offre)"}).text
                job["contract"] = _contract if _contract else "-"
                job["status"] = "cadre"

                jobs_list.append(job)
            except Exception as e:
                warning(e)
        return jobs_list

    def next_search_page(self):

        sleep(SLEEP * 2)
        url = self.current_url
        if self.page_nb == 0:
            url += f"&page=1"
        else:
            url = url.replace(f"page={self.page_nb}", f"page={self.page_nb+1}")
        self.page_nb += 1
        self.get(url)
        info(url)
        sleep(SLEEP * 2)

    def candidate(self, url):

        # connexion
        if not self.connected:
            raise AttributeError("Not connected")

        if url[0] == "/":
            url = url[1:]

        # get if needed
        url = "https://cadres.apec.fr/" + url
        if self.current_url != url:
            self.get(url)
            sleep(SLEEP * 3)

        # soup = BeautifulSoup(self.page_source)
        # _soup = soup.find_all("a", attrs={"class": "button-flat-blue"})

        button = self.find_element_by_class_name("button-flat-blue full-width text-uppercase text-center ng-scope")
        button.click()
        return True, "reached", "success"
