#!/usr/bin/env python3
# coding: utf-8


from sultan import os, webdriver, re


deja_postule = 'https://www.linkedin.com/jobs/view/1201801606/'
postuler = 'https://www.linkedin.com/jobs/view/1183675536/'
candidature_simplifiee = 'https://www.linkedin.com/jobs/view/1225757484/'


class Linkedin(webdriver.Firefox):

    def __init__(self):
        """init method"""

        url = "https://fr.linkedin.com"
        super().__init__()
        self.get(url)
        self.first_url = url
        self.jobs = []
        # self._jobs = pd.DataFrame(columns=["id", "job", "company", "plateform", "url", "real_url", "applied", "loc", "salary", "date"])

        sleep(1)
        info("lindedin reached")

    def login(self, e_mail, passwd):
        """login with email and password"""

        assert isinstance(e_mail, str)
        if not re.match(r"[^@]+@[^@]+\.[^@]+", e_mail):
            raise AttributeError("invalid email")
        assert isinstance(passwd, str)

        # attributes
        self.username = e_mail
        self.password = passwd

        # elements
        _username = self.find_element_by_id("login-email")
        _passwd = self.find_element_by_id("login-password")

        time.sleep(1)
        _username.send_keys(e_mail)
        time.sleep(1)
        _passwd.send_keys(passwd)
        time.sleep(1)
        self.find_element_by_id("login-submit").click()
        time.sleep(1)
        if not "https://www.linkedin.com/feed/" == self.current_url:
            raise AttributeError("username or passwd do not match OR"
                                 " inter page between login and feed")
        info("linkedin connected")

    def search(self, words, loc, pages=5):
        """peform a search and retur the list of jobs"""

        # check args
        assert isinstance(words, str)
        assert isinstance(loc, str)
        loc = loc.title()

        def _search():
            """just type words and loc and enter + wait time to load"""

            # go to  search page
            self.get("https://www.linkedin.com/jobs/search/")
            info("reached search page")
            time.sleep(1)
            # find and send resach keys
            _words = self.find_element_by_id("jobs-search-box-keyword-id-ember90")
            _words.clear()
            _words.send_keys(words)
            _words.send_keys(Keys.ENTER)
            info("send words")
            time.sleep(1)
            _loc = self.find_element_by_id("jobs-search-box-location-id-ember90")
            _loc.clear()
            _loc.send_keys(loc)
            _loc.send_keys(Keys.ARROW_DOWN)
            _loc.send_keys(Keys.ENTER)
            info("send loc")
            time.sleep(2)

        def _scroll(downs=500):
            """perform a manual scroll of the web page"""

            soup = BeautifulSoup(self.html)
            _soup = soup.find_all("div", attrs={"data-control-name":
                                                "A_jobssearch_job_result_click"})
            last_id = _soup[-1].attrs["id"]
            button = self.find_element_by_id(last_id)
            button.click()
            for i in range(downs):
                button.send_keys(Keys.ARROW_DOWN)
            info("scroll done")
            time.sleep(2)

        # extract jobs
        def _extract_jobs():
            """ create a soup and extract jobs from html"""

            soup = BeautifulSoup(self.page_source)
            _soup = soup.find_all("div", attrs={"data-control-name":
                                                "A_jobssearch_job_result_click"})

            def _ref(s): return "https://www.linkedin.com/jobs/view/" \
                + s.attrs["data-job-id"].split(":")[-1]

            def _job(s): return (s.h3.get_text()).strip().lower().replace("promu", "").replace("\n", "").replace("H/F", "").replace("(H/F)", "").replace("F/H", "").strip().title()

            def _company(s): return s.h4.get_text().strip()

            def _id(s): return s.attrs["data-job-id"].split(":")[-1]

            self.jobs.extend([(_job(s), _company(s), _ref(s), _id(s)) for s in _soup])

        # main page 1
        _search()
        _scroll()
        _extract_jobs()

        # other pages
        for i in range(2, 2 + N):
            _page = f"Page {i}"
            button = self.find_element_by_xpath(f"//button[@aria-label='{_page}']")
            button.click()
            time.sleep(2)
            _scroll()
            _extract_jobs()

        info("lindedin search performed")
        info(self.jobs)
        info(len(self.jobs))

    def apply(self, url):
        """apply to one job offer"""

        _url = self.current_url

        self.get(url)
        time.sleep(2)
        soup = BeautifulSoup(self.html)
        buttons = soup.find_all("button")
        candidature_simplifiee = [i for i in buttons
                                  if "Candidature simplifiée" in i.get_text()]
        postuler = [i for i in buttons if "Postuler" in i.get_text()]
        a = soup.find_all("a")
        deja_postule = [i for i in a if "Voir la candidature" in i.get_text()]

        if not (postuler or candidature_simplifiee or deja_postule):
            raise AttributeError(" no possible to candidature, no already candidature")

        if candidature_simplifiee:
            # web page
            job_id = url.split("/")[-1]
            button = self.find_element_by_xpath(f"//button[@data-job-id='{job_id}']")
            button.click()
            time.sleep(1)

            # popup
            button = self.find_element_by_xpath(f"//button[@type='submit']")
            button.click()
            time.sleep(1)

        elif postuler:
            # web page
            soup = BeautifulSoup(self.html)
            buttons = soup.find_all("button")
            buttons = [i for i in buttons if "Postuler" in i.get_text()]
            button = buttons[0]
            _button = self.find_element_by_id(button.attrs["id"])
            _button.click()

            # popup
            soup = BeautifulSoup(self.html)
            buttons = soup.find_all("button")
            buttons = [i for i in buttons if "Continuer" in i.get_text()]
            button = buttons[0]
            _button = self.find_element_by_id(button.attrs["id"])
            _button.click()

            if len(self.window_handles) > 1:
                warning("error, a new tab opened for this job")
                # close 2nd tab
                handles = self.window_handles
                self.switch_to.window(handles[1])
                self.close()

        self.get(_url)

    # def apply_all(self) :
    #     "apply to all jobs"
    #
    #     _url = self.current_url
    #
    #     for url in [job[2] for job in  self.jobs] :
    #         self.get(url)
    #         time.sleep(3)
    #
    #     self.get(_url)
    #     info("linkedin apply")

    @property
    def html(self):
        return self.page_source

    @html.setter
    def html(self, arg):
        raise ValueError("no autorised to change html")


# # with Linkedin() as lkd :
# self = Linkedin()
# self.login("a_syoez@yahoo.fr", "201186Aa")
# self.search("python", "Paris")
# #     lkd.apply()
