import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InputCharacters:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.search_bar = '//input[@name="q"]'
        self.search_button = '//input[@class="gNO89b"]'
        self.result_text = '//h3[@class="LC20lb MBeuO DKV0Md"]'
        self.google_terms = '//div[@id="CXQnmb"]'
        self.decline_button = '//button[@id="W0wltc"]'
        self.agree_button = '//button[@id="L2AGLb"]'
        self.driver = driver

    def check_search_result(self, characters: str) -> int:
        self.run_search(characters)
        count_results = len(self.driver.find_elements(By.XPATH, self.result_text))
        return count_results

    def select_google_terms(self, agree: str = 'y'):
        if agree == 'y':
            self.driver.find_element(By.XPATH, self.agree_button).click()
        if agree == 'n':
            self.driver.find_element(By.XPATH, self.decline_button).click()

    def run_search(self, chars: str = 'google'):
        search = self.driver.find_element(By.XPATH, self.search_bar)
        search.send_keys(chars)
        search.submit()