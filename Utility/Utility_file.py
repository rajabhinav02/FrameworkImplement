import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class Baseclass:

    def Wait(self,locator):
        wait = WebDriverWait(self.driver, 15)

        #wait.until(expected_conditions.presence_of_element_located((By.XPATH, text)))
        wait.until(expected_conditions.presence_of_element_located(locator))

    def dropdown(self, locator, text):
        select = Select(locator)
        select.select_by_visible_text(text)











