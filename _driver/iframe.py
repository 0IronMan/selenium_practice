from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")
url=r"file:///C:/Users/sanji/Downloads/frames.html"
# driver.get(url)
# driver.maximize_window()
# sleep(3)
# driver.switch_to.frame("frame2")
# driver.find_element(By.LINK_TEXT, "About Selenium").click()












# from selenium import webdriver
# from selenium.webdriver.common.by import By
# driver=webdriver.Chrome(r"C:\Users\Admin\PycharmProjects\pythonProject\QPSM1\driver\chromedriver.exe")
# #url=r"https://www.amazon.in/mobile-phones"
# url=r"file:///C:/Users/Admin/Downloads/frames.html"
driver.get(url)
driver.switch_to.frame("frame2")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@class='selenium-button selenium-webdriver text-uppercase font-weight-bold']").click()