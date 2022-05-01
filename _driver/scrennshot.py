# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome(r"C:\Users\sanji\PycharmProjects\selenium_practice\_driver\chromedriver.exe")
# url = r"http://demo.actitime.com/login.do"
# driver.get(url)
# driver.maximize_window()
# driver.save_screenshot(r"C:\Users\sanji\PycharmProjects\selenium_practice\screenshot\before.png")
# driver.find_element(By.ID, "username").send_keys("sanjit")
# driver.find_element(By.NAME, "pwd").send_keys("patel")
# driver.get_screenshot_as_file("after_sending_keys.png")
# driver.find_element(By.XPATH, "//div[text()='Login ']").click()
l = [6, 2, 3, 5]
out = []
for i in l:
    r = 0
    if i > r:
        r = i
        out +=[i]
    else:
        out= [i] + [out]

print(out)
print(r)