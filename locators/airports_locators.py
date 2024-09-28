from selenium.webdriver.common.by import By

class AirportsPageLocators:
    PAGE_ADDR = (By.XPATH, '//*[@id="aAirports"]')
    ADD_AIRPORT_BTN = (By.XPATH, '//*[@id="btnNewAirport"]')
    NEW_AIRPORT_CODE = (By.XPATH, '//*[@id="airportCode"]')
    NEW_AIRPORT_NAME = (By.XPATH, '//*[@id="airportName"]')
    NEW_AIRPORT_CITY = (By.XPATH, '//*[@id="city"]')
    NEW_AIRPORT_REGION = (By.XPATH, '//*[@id="state"]')
    NEW_AIRPORT_COUNTRY = (By.XPATH, '//*[@id="country"]')
    NEW_AIRPORT_SAVE_BTN = (By.XPATH, '//*[@id="btnSave"]')
    NAME_AIRPORT_LIST = (By.XPATH, '/html/body/div[3]/div[1]/div[1]/h1')