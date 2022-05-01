from page_objects.LoginPage import LoginPage
from time import sleep

#
# class Test_001_login:
#     base_url = "https://www.instagram.com/"
#     username = "black_lover_o1"
#     password = "Sanjit@123"
#
#     def test_homepagetitle(self, setup):
#         self.driver = setup
#         self.driver.get(self.base_url)
#         sleep(3)
#         act_title = self.driver.title
#         if act_title == "your store. Login":
#             assert True
#         else:
#             self.driver.save_screenshot("test_homepagetitle.png")
#             assert False
#         self.driver.close()
#
#     def test_login(self, setup):
#         self.driver = setup
#         self.driver.get(self.base_url)
#         self.lp = LoginPage(self.driver)
#         sleep(3)
#         self.lp.setUsername(self.username)
#         sleep(3)
#         self.lp.setpassword(self.password)
#         sleep(3)
#         self.lp.clickLogin()
#         sleep(2)
#         act_title = self.driver.title
#
#         if act_title == "dashboard / nopCommerce administration":
#             assert True
#         else:
#             self.driver.save_screenshot(r"C:\Users\sanji\PycharmProjects\selenium_practice\screenshot\test_login.png")
#             assert False
#         self.driver.close()

class Test_001_Login:
    base_url = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

    def test_homepagetitle(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)
        sleep(3)
        act_title = self.driver.title
        if act_title == "your store. Login":
            assert True
        else:
            self.driver.save_screenshot("test_homepagetitle.png")
            assert False
        self.driver.close()

    def test_login(self, setup):
        self.driver =setup
        self.driver.get (self.base_url)
        self.lp.LoginPage(self.driver)
        self.lp.setUsername (self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title== "Dashboard / nopCommerce administration":

        if act_title="Dashboard / nopCommerce administration":
            assert True
        else:
            self.driver.save_screenshot(
            r"C:\Users\Rachana\PycharmProjects\python Project\python Project2\page_object_module\screen_shots\test_login.png")
        assert False
            self.driver.close()
