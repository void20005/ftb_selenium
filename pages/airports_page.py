import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.conftest import driver
from pages.base_page import BasePage
from locators.airports_locators import AirportsPageLocators as Locators

class Airports(BasePage):
    def add_airports_button(self):
        self.click_element(Locators.ADD_AIRPORT_BTN)
