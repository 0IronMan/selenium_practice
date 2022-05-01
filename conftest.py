from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")

# @pytest.fixture()
# def test_setup():
#     url=r"https://www.amazon.in/"
#     driver.get(url)
#     driver.maximize_window()
#     print("test seteup executed")
#     yield
#     driver.close()
#     print("execution done")

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")
    return driver