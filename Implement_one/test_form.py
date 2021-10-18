import time

import pytest

from selenium.webdriver.support.select import Select

from Page_Object_Model.HomePage import Homepage
from Utility.Utility_file import Baseclass
from test_data.homepagedata import Homepagedata


class Testform(Baseclass):

    def test_form(self, data):
        newhomepage = Homepage(self.driver)

        newhomepage.getName().send_keys(data["first name"])#data[0])
        newhomepage.getEmail().send_keys(data["second name"])
        newhomepage.getpwd().send_keys(data["email"])
        newhomepage.getcheckbox().click()
        #sele=newhomepage.getGender()
        ##sele= Select(newhomepage.getGender())
        #sele.select_by_visible_text("Female")

        #selec=self.dropdown(newhomepage.getGender())
        #selec.select_by_visible_text("Female")

        self.dropdown(newhomepage.getGender(),"Female")

        empstatuses = newhomepage.getEmpStatus()
        #empstatuses[0].click()
        for emp in empstatuses:
            emp.click()
            time.sleep(4)

        assert not empstatuses[2].is_enabled()
        #print (newhomepage.getmsg().text)

        newhomepage.getSubmitButton().click()

        assert "Success" in newhomepage.getmsg().text
        self.driver.refresh()



@pytest.fixture(params= Homepagedata.td)
def data(request):
    return request.param


