
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait




#@pytest.mark.usefixtures("openBrowser")
from Page_Object_Model.Checkout import Checkout
from Page_Object_Model.ConfirmPage import Confirm
from Page_Object_Model.HomePage import Homepage
from Page_Object_Model.OrderPage import Order
from Utility.Utility_file import Baseclass


class TestFirst(Baseclass):
    #homepage = Homepage(self.driver)

    def test_ee(self):
        #List=[]
        homepage = Homepage(self.driver)
        #checkout = Checkout(self.driver)
        #orderlist = Order(self.driver)
        #confirm = Confirm(self.driver)
        #homepage.getshop().click()
        checkout=homepage.getshop()
        #addbuttons= checkout.getButtons()


        #addbuttons = self.driver.find_elements_by_css_selector(".btn-info")
        addbuttons= checkout.getAddGuttons()

        for add in addbuttons:

            #name= checkout.getname().text
            name=add.find_element_by_xpath("parent:: div/ parent::div/div[1]/h4/a").text
            if name == "Blackberry":
                add.click()


        orderlist= checkout.getCheckutButton()
    #def test_e2e2(self):
        #orderlist= Order(self.driver)
        name2= orderlist.getselectedname().text

        assert name2 == name

        print (name2)

        quantity=orderlist.getquantity().text
        print(quantity)
        price= orderlist.getpricevalue().text
        print(price)
        total= orderlist.gettotalvalue().text
        print(total)

        #try:
        #with pytest.raises(ValueError) as esc:
            #assert int(quantity)*int(price)==int(total), "haha"

        #print (str(esc))
        #except:
            #pytest.fail("test case failed", pytrace=True)



        confirm=orderlist.getConfirmbutton()

        confirm.getcountrytext().send_keys("I")



        #self.Wait("//div/div[2]/ul/li/a")
        self.Wait(confirm.countries)

        #wait=WebDriverWait(self.driver,15)

        #wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div/div[2]/ul/li/a")))

        countries= confirm.getCountries()

        #List.append(countries)
        #print(List)
        for country in countries:
            if country.text == "India":
                country.click()
                break

        confirm.getsubmitbutton().click()
        print(confirm.getfinalmssg())
        assert "Success" in confirm.getfinalmssg().text

        self.driver.get_screenshot_as_file("Final.png")


