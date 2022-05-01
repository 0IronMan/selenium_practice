from selenium import webdriver
driver=webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")
url=r"http://demowebshop.tricentis.com/"
driver.get(url)
driver.maximize_window()
cookies=driver.get_cookies()
for cookie in cookies:
    print(cookie)

add={'name':'PYSPYDER', 'value':'BASANVANAGUDI'}
driver.add_cookie(add)
for cookie in cookies:
    print(cookie)

print("added")
print(driver.get_cookie("PYSPYDER"))
print("deleting")
driver.delete_cookie("PYSPYDER")
cookies=driver.get_cookies()
for cookie in cookies:
    print(cookie)
print("deleted specified cookie")
driver.delete_all_cookies()
print("deleted all cookies")
cookies=driver.get_cookies()
for cookie in cookies:
    print(cookie)