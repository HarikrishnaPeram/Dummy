import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        Ewait = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))
    def SelectOptionBytext(self, locator,text,driver):
        sel = Select(locator)
        sel.select_by_visible_text(text)
        #self.driver.switch_to_alert().accept()
        alert = self.alert=driver.switch_to.alert
        alert.accept()


