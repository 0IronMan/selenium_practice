from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")

#simple alert

# url = r"file:///C:/Users/sanji/Downloads/simple_alert.html"
# driver.get(url)
# driver.maximize_window()
#
# driver.find_element(By.TAG_NAME, "button").click()
# sleep(2)
# driver.switch_to.alert.accept()

#confirmation alert

# url = r"file:///C:/Users/sanji/Downloads/con_alert.html"
# driver.get(url)
# driver.maximize_window()
#
# driver.find_element(By.TAG_NAME, "button").click()
# sleep(3)
# driver.switch_to.alert.accept()
# sleep(2)
# driver.refresh()
# driver.find_element(By.TAG_NAME, "button").click()
# sleep(3)
# driver.switch_to.alert.dismiss()


#prompt alert

url = r"file:///C:/Users/sanji/Downloads/prompt.html"
driver.get(url)
driver.maximize_window()
sleep(2)
driver.find_element(By.TAG_NAME, "button").click()
sleep(2)
# driver.switch_to.alert.accept()
driver.switch_to.alert.send_keys("sanjit")
driver.switch_to.alert.accept()