from selenium.webdriver.common.by import By

class LoginPageLocators:
    Username = (By.XPATH,'//*[@id="txtUsername"]')
    Password = (By.XPATH,'//*[@id="txtPassword"]')
    SignIn_button = (By.XPATH,'//*[@id="btnSubmit"]')
    Plane = (By.XPATH,'//*[@id="btnLogout"]')