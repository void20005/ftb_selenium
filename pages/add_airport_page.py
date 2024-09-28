import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from tests.conftest import driver
from pages.base_page import BasePage
from locators.airports_locators import AirportsPageLocators as Locators

class Add_Airport(BasePage):
    def fill_fields(self, data):
        self.enter_text(Locators.NEW_AIRPORT_CODE,data['airport_code'])
        self.enter_text(Locators.NEW_AIRPORT_NAME,data['airport_name'])
        self.enter_text(Locators.NEW_AIRPORT_CITY,data['airport_city'])
        self.enter_text(Locators.NEW_AIRPORT_REGION,data['airport_region'])
        self.enter_text(Locators.NEW_AIRPORT_COUNTRY,data['airport_country'])
        
    def new_airports_save_button(self):
        self.click_element(Locators.NEW_AIRPORT_SAVE_BTN)
    
    