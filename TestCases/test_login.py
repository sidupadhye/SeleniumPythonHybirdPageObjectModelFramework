import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=Readconfig.getApplicationURL()
    username=Readconfig.getUsername()
    password=Readconfig.getPassword()

    logger=LogGen.loggen()

    def test_homePageLogin(self,setup_and_teardown):

        self.logger.info("*****************Test_001_Login********************")
        self.logger.info("***************Verifying Home Page Title***********")
        self.driver=setup_and_teardown
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            #self.driver.close()
            self.logger.info("***************Home Page Title is passed***************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageLogin.png")
            self.driver.close()
            self.logger.info("************Home Page title is Failed****************")
            assert False

    def test_login_with_valid_credentials(self,setup_and_teardown):
        self.logger.info("*****************Test Login with valid credentials*********")
        self.logger.info("************Verifying Login Test*************************")
        self.driver=setup_and_teardown
        self.driver.maximize_window()
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setUserPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            #self.driver.close()
            self.logger.info("**********Login test Passed********************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Login_with_valid_credentials.png")
            self.driver.close()
            self.logger.info("*************Login Test Failed*******************")
            assert False

