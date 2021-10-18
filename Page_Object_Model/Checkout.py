from selenium.webdriver.common.by import By

from Page_Object_Model.OrderPage import Order


class Checkout:

    def __init__(self, driver):
        self.driver = driver

    AButtons = (By.XPATH,"//button[@class='btn btn-info']")
    ChButtons= (By.XPATH,"//a[contains(@class, 'btn-primary')]")
    #print(AButtons(1))
    #AB= (By.XPATH,"//button[@class='btn btn-info']")
    #CD = "/parent::div/parent::div/div/h4"
    #AB(1)+CD
    ##name = (By.XPATH, "parent::div/parent::div/div/h4")

    def getButtons(self):
        return self.driver.find_elements(*Checkout.AButtons)

    def getCheckutButton(self):
        #return self.driver.find_element(*Checkout.ChButtons)
        self.driver.find_element(*Checkout.ChButtons).click()
        orderlist = Order(self.driver)
        return orderlist

    def getAddGuttons(self):
        return self.driver.find_elements(*Checkout.AButtons)

    #def getname(self):
        #return self.AButtons.find_element(*Checkout.name)



 #   add.find_element_by_xpath("parent:: div/ parent::div/div[1]/h4/a").text
