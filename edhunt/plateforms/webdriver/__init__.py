from edhunt.plateforms.webdriver.apec import Apec
from edhunt import db, warning


class _WebDriver:
    apec = Apec


class WebDriver:

    def test_connexion(plateform):

        plateform_name = plateform.__name__.lower().strip()

        Driver = getattr(_WebDriver, plateform_name)
        driver = Driver()

        if plateform_name == "apec":
            d = {"status": plateform.status}
        else:
            d = dict()

        res, msg, color = driver.test_connexion(plateform.email,
                                                plateform.password,
                                                **d)

        if plateform_name == "apec":
            plateform.status = driver.status
            db.session.commit()
        driver.close()
        return res, msg, color

    def search_light(plateform, words, loc, pages=3):

        plateform_name = plateform.__name__.lower().strip()

        Driver = getattr(_WebDriver, plateform_name)
        driver = Driver()

        if plateform_name == "apec":
            d = {"status": plateform.status}
        else:
            d = dict()

        driver.login(plateform.email, plateform.password, **d)
        res, msg, color = driver.perform_search_light(words, loc)

        opportunities_list = list()
        if res:
            for i in range(pages):
                res = driver.scrap_search_light()
                if not res:
                    break
                opportunities_list.extend(res)
                driver.next_search_page()

        driver.close()

        return opportunities_list, "OK for search_light", color

    def candidate(plateform, url):

        plateform_name = plateform.__name__.lower().strip()

        Driver = getattr(_WebDriver, plateform_name)
        driver = Driver()

        if plateform_name == "apec":
            d = {"status": plateform.status}
        else:
            d = dict()

        driver.login(plateform.email, plateform.password, **d)

        res, msg, color = driver.candidate(url)

        return res, msg, color
