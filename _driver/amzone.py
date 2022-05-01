from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")

url=r"https://www.amazon.in/"
driver.get(url)
driver.maximize_window()
print("test seteup executed")










driver.find_element(By.CLASS_NAME,"hm-icon-label").click()
driver.find_element(By.XPATH,"//a[text()='Sign In']").click()
driver.find_element(By.ID, "ap_email").send_keys("1234567890")
driver.find_element(By.ID, "continue").click()