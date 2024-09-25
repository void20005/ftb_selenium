import os
import logging
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
from locators.login_locators import LoginPageLocators


# Load environment variables from .env file
load_dotenv()
url = os.getenv('APP_URL')+'login'
login = os.getenv('APP_USERNAME')
password = os.getenv('APP_PASSWORD')
assert url is not None, "APP_URL не загружен"
assert login is not None, "USERNAME не загружен"
assert password is not None, "PASSWORD не загружен"
logging.debug(f"URL: {url}, Username: {login}, Password: {password}")
def test_login(driver): 
    login_page = LoginPage(driver, url = url)  
    login_page.open()   
    # Submit login form with valid credentials
    login_page.submit_login(login, password)
    # Verify that login was successful by checking for an element present after login
    assert login_page.is_element_present(LoginPageLocators.Plane)