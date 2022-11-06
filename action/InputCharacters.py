import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from variables.PageElement import PageElement


class InputCharacters:

    def __init__(self, driver):
        self.wait = WebDriverWait(driver, 10)
        self.page_element = PageElement
        self.driver = driver

    def check_search_result(self, run_with_cookie: str = 'agree_terms') -> list:
        results = []
        for element in self.page_element.CHARACTERS:
            item = [{'Element': element}]
            self.run_search(element)
            text_results = self.driver.find_elements(By.XPATH, self.page_element.RESULT_TEXT)
            item.append('Result for element: ' + element + ' not found.')
            self.driver.execute_script('document.body.style.zoom="50%"')
            self.driver.save_screenshot('./logs/images/'+run_with_cookie+'/characters/item_' + element + '_log.png')
            count = 0
            for text_result in text_results:
                item.append({'nr': count, 'text': text_result.text})
                count += 1
            results.append(item)
            self.driver.back()
        return results

    def run_search(self, chars: str = 'google'):
        search = self.driver.find_element(By.XPATH, self.page_element.SEARCH_BAR)
        search.send_keys(chars)
        search.submit()