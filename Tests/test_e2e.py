from selenium.webdriver.support.select import Select

from Tests.BaseClass import BaseClass
from Tests.BasicInfo import BasicInfo


class TestFacebook(BaseClass):
    def test_e2e(self):
        basicinfo = BasicInfo(self.driver)