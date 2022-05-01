from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")

url = r"file:///C:/Users/sanji/Downloads/standard_listbox.html"
# url=r"file:///C:/Users/sanji/Downloads/loading.html"
driver.get(url)
driver.maximize_window()
# driver.implicitly_wait(20)
# driver.find_element(By.NAME, "fname").send_keys("manu")
driver.find_eleme(By.ID, "standard_cars").click()
driver.find_element_by_xpath("//option[@value='2']//following::[1]]").click()