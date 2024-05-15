from selenium import webdriver
import pytest
from pageObjects.LoginPage import Login
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig


class Test_001_LoginPage:
    baseurl = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.logger()

    @pytest.mark.sanity
    def test_homePageTitle(self, setup):
        self.logger.info("******************Test_001_LoginPage******************")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("****************** test_homePageTitle test is PASSED ******************")
        else:
            self.logger.info("****************** test_homePageTitle test is FAILEd ******************")
            assert False

    @pytest.mark.regression
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        lp = Login(self.driver)
        lp.setUsername(self.username)
        lp.setPassword(self.password)
        lp.clickLogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
        else:
            assert False
