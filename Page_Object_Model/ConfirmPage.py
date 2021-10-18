from selenium.webdriver.common.by import By


class Confirm:

    def __init__(self, driver):
        self.driver = driver

    countrytext = (By.CSS_SELECTOR, "#country")
    submitbutton = (By.XPATH, "//input[@type='submit']")
    finalmssg = (By.XPATH, "//strong")
    countries = (By.XPATH, "//div/div[2]/ul/li/a")


    def getcountrytext(self):
        return self.driver.find_element(*Confirm.countrytext)

    def getsubmitbutton(self):
        return self.driver.find_element(*Confirm.submitbutton)


    def getfinalmssg(self):
        return self.driver.find_element(*Confirm.finalmssg)

    def getCountries(self):
        return self.driver.find_elements(*Confirm.countries)