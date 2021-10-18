from selenium.webdriver.common.by import By

from Page_Object_Model.ConfirmPage import Confirm


class Order:

    def __init__(self, driver):
        self.driver= driver

    selectedname= (By.XPATH,"//h4[@class='media-heading']/a")
    quantitycount = (By.CSS_SELECTOR,"#exampleInputEmail1")
    pricevalue = (By.XPATH,"//tr/td[3]/strong")
    totalvalue = (By.XPATH, "//tr/td[4]/strong")
    confirmbutton = (By.CSS_SELECTOR,".btn-success")

    def getselectedname(self):
        return self.driver.find_element(*Order.selectedname)

    def getquantity(self):
        return self.driver.find_element(*Order.quantitycount)

    def getpricevalue(self):
        return self.driver.find_element(*Order.pricevalue)

    def gettotalvalue(self):
        return self.driver.find_element(*Order.totalvalue)

    def getConfirmbutton(self):
        #return self.driver.find_element(*Order.confirmbutton)
        self.driver.find_element(*Order.confirmbutton).click()
        confirm= Confirm(self.driver)
        return confirm