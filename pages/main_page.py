import logging
import os
from dotenv import load_dotenv
from pages.base_page import BasePage
from locators.main_locators import MainPageLocators as Locators



class main_page(BasePage):
    
    def main_page(self):
        self.click_element(Locators.MAIN_PAGE)

    def airports(self):
        self.click_element(Locators.AIRPORTS)

    def aircrafts(self):
        self.click_element(Locators.AIRCRAFTS)

    def flights(self):
        self.click_element(Locators.FLIGHTS)

        
