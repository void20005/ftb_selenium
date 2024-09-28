import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    #options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

    # WebDriverWait(driver, 10).until(EC.url_changes("/login"))
    #options.add_argument('--window-size=1600,1200')
    options.add_argument('--start-maximized')
    # options.add_argument('--headless')
    # driver.maximize_window() 
    driver = webdriver.Chrome(options=options)
    # Return the WebDriver instance
    yield driver
    driver.quit()