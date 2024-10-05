from selenium import webdriver
from utilities.customLogger import LogGen
from utilities.readProperties import Readconfig
from utilities import XLutils
from PageObjects.LoginPage import LoginPage

class Test_002_DDT_Login:
    baseURL=Readconfig.getApplicationURL()
    path=".//TestData//logindata.xlxs"
    logger=LogGen.loggen()

    def test_login_ddt(self,setup_and_teardown):
        self.logger.info("******Test_002_DDT_Login*******")
        self.logger.info("******verifying Login DDT Test***********")
        self.driver=setup_and_teardown
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
