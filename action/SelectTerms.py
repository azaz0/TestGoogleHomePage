from selenium.webdriver.common.by import By


class SelectTerms:

    def __init__(self, driver):
        self.google_terms = '//div[@id="CXQnmb"]'
        self.decline_button = '//button[@id="W0wltc"]'
        self.agree_button = '//button[@id="L2AGLb"]'
        self.driver = driver

    def select_google_terms(self, agree: str = 'y'):
        if agree == 'y':
            self.driver.find_element(By.XPATH, self.agree_button).click()
        if agree == 'n':
            self.driver.find_element(By.XPATH, self.decline_button).click()
