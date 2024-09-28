import os
import logging
import pytest
from dotenv import load_dotenv
from pages.login_page import LoginPage
from pages.airports_page import Airports
from pages.add_airport_page import Add_Airport
from locators.airports_locators import AirportsPageLocators as APL
from data.data_generator import generate_airport_data
from pages.main_page import main_page
from pages.airports_page import Airports
from selenium.webdriver.common.by import By

# Load environment variables from .env file
load_dotenv()
url = os.getenv('APP_URL')
login = os.getenv('APP_USERNAME')
password = os.getenv('APP_PASSWORD')

assert url is not None, "APP_URL not loaded"
assert login is not None, "APP_USERNAME not loaded"
assert password is not None, "APP_PASSWORD not loaded"
logging.debug(f"URL: {url}, Username: {login}, Password: {password}")

def test_create_airport_valid_data(driver):
    # Log in
    login_page = LoginPage(driver, url=url + "login")
    login_page.open()
    login_page.submit_login(login, password)
    main_pg = main_page(driver)
    main_pg.airports()
    airports_pg = Airports(driver)
    airports_pg.add_airports_button()  
    # Fill in the airport data on the add airport page
    add_airport_page = Add_Airport(driver)
    # Generate random data for a new airport
    data = generate_airport_data()
    add_airport_page.fill_fields(data)
    # Click the "Save" button (assuming you have a method for this in your page object)
    add_airport_page.new_airports_save_button()
    airports_pg = Airports(driver)
    assert airports_pg.is_element_present(APL.NAME_AIRPORT_LIST), "Airport hasn't been added"

##################################
    airport_code = data['airport_code']
    current_page_number = 0
    result_page = 0
    while True:
        print(f"Looking for an airport with code: {airport_code} on cureent page...")             
        rows = driver.find_elements(By.CSS_SELECTOR, '#tblAirports tbody tr')# !!!!!!!!!!
        current_page_number = current_page_number + 1   
        for row in rows:
            if not rows:
                break
            code_cell = row.find_element(By.XPATH, './td[1]')# !!!!!!!!!!
            print(f"Verifying the airportCode: {code_cell.text}")
            if code_cell.text == airport_code:
                print(f"Airport is found. Aiport code: {airport_code}")
                result_page = current_page_number
                break
        print(f"Current page: {result_page}")
        if result_page:
            break
        driver.get(url + "airports?pageNo=" + str(current_page_number))
    assert result_page, "Airport was added successfully."
