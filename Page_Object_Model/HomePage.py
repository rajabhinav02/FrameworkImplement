from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Page_Object_Model.Checkout import Checkout


class Homepage:


    Shop = (By.LINK_TEXT,"Shop")
    name= (By.XPATH, "//form[contains(@class, ng-invalid)]/div[1]/input")
    email= (By.XPATH, "//input[@name='email']")
    pwd = (By.XPATH, "//input[@type='password']")
    chkbox = (By.CSS_SELECTOR, "[type='checkbox']")
    sel=(By.CSS_SELECTOR,"#exampleFormControlSelect1")
    rb= (By.CSS_SELECTOR, "[type = 'radio']")
    submit= (By.CSS_SELECTOR, "[class*=btn]")
    textmsg = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")


    def __init__(self, driver):
        self.driver= driver

    def getshop(self):
        # return self.driver.find_element(*Homepage.Shop)
        # commenting for more implementation of POM
        self.driver.find_element(*Homepage.Shop).click()
        checkouts= Checkout(self.driver)
        return checkouts

    def getName(self):
        return self.driver.find_element(*Homepage.name)

    def getEmail(self):
        return self.driver.find_element(*Homepage.email)

    def getpwd(self):
        return self.driver.find_element(*Homepage.pwd)

    def getcheckbox(self):
        return self.driver.find_element(*Homepage.chkbox)

    def getGender(self):

        #selectvalue = Select(self.driver.find_element(*Homepage.sel))
        #return selectvalue

        return self.driver.find_element(*Homepage.sel)

    def getEmpStatus(self):

        return self.driver.find_elements(*Homepage.rb)

    def getSubmitButton(self):

        return self.driver.find_element(*Homepage.submit)

    def getmsg(self):
        return self.driver.find_element(*Homepage.textmsg)

