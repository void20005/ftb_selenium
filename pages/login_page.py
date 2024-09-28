import logging
import os
from dotenv import load_dotenv
from pages.base_page import BasePage
from locators.login_locators import LoginPageLocators as Locators



class LoginPage(BasePage):
    def submit_login(self, userName, password):
        self.logger.info("Submitting login form")
        # Enter Login
        self.enter_text(Locators.Username, userName, 10)
        # Enter password
        self.enter_text(Locators.Password, password, 10)
        # Click the login button
        self.click_element(Locators.SignIn_button, 10)

