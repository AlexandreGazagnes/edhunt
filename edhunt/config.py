import json


with open("/etc/edhunt.json") as file:
    config = json.load(file)


class Params():
    TEST_MODE = False  # False
    FORCE_QUESTIONNAIRE = True  # True
    DISABLE_USER = True

    DISABLE_REGISTER = True
    DISABLE_LOGIN = False

    CORPORATE_PASSWORD = "edhuntcesttr0pbien!"
    HEADLESS_WEB_DRIVER = True


class Config():
    SECRET_KEY = config.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = 'smtp.googlemail.com'
    MAIL_USERNAME = config.get("EMAIL_USER")
    MAIL_PASSWORD = config.get("EMAIL_PASS")


class Alex():
    EMAIL = config.get("ALEX_EMAIL")
    PASSWORD = config.get("ALEX_PASSWORD")
    APEC_EMAIL = config.get("ALEX_APEC_EMAIL")
    APEC_PASSWORD = config.get("ALEX_APEC_PASSWORD")
