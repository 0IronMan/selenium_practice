from conftest import *
from selenium.webdriver.common.by import By

def test_login(test_setup):
    driver.find_element(By.CLASS_NAME, "hm-icon-label").click()
    driver.find_element(By.XPATH, "//a[text()='Sign In']").click()
    driver.find_element(By.ID, "ap_email").send_keys("1234567890")
    driver.find_element(By.ID, "continue").click()
