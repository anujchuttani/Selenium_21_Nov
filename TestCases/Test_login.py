import pytest
from selenium import webdriver
from pageObject.loginPage import loginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUsrEmail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_homepagetitle(self, setup):

        self.logger.info("**************Test_001_Login************************")
        self.logger.info("**************Verifying_HOME_PAGE_Title*************")

        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("****** ** ** ** ** Home_Page_Title test is passed ** ** ** ** ** ** *")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homepagetitle.png")
            assert False
            self.driver.close()
            self.logger.info("****** ** ** ** ** Home_Page_Title test is failed ** ** ** ** ** ** *")

    def test_login(self, setup):
        self.logger.info("**************Verifying_Login Page*************")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = loginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**************Verifying_Login Page Passed*************")
        else:
            assert False
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_login.png")
            self.driver.close()
            self.logger.info("**************Verifying_Login Page Failed*************")
