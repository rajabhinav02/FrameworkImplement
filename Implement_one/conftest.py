import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")

def setup(request):
    browser_name= request.config.getoption("--browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\chromedriver_win32\\chromedriver.exe")
    elif browser_name == "edge":
        driver = webdriver.Chrome(executable_path="C:\\edgedriver_win64\\msedgerdriver")

    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()

    request.cls.driver=driver
    #yield
    #driver.close()

