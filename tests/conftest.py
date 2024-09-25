import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    # options.add_argument('--window-size=1600,1200')
    # options.add_argument('--headless')
    # driver.maximize_window() 
    
    # Return the WebDriver instance
    yield driver
    driver.quit()