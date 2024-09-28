from selenium.webdriver.common.by import By

class MainPageLocators:
    MAIN_PAGE = (By.XPATH,'//*[@id="aHome"]')
    AIRPORTS = (By.XPATH,'//*[@id="aAirports"]')
    AIRCRAFTS = (By.XPATH,'//*[@id="aAircrafts"]')
    FLIGHTS = (By.XPATH,'//*[@id="aFlights"]')