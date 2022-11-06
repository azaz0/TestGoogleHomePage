from variables.Endpoints import Endpoints
from variables.PageElement import PageElement


class SearchEndpoint:

    def __init__(self, driver):
        self.page_element = PageElement
        self.endpoints = Endpoints.TEST_ENDPOINT
        self.driver = driver

    def check_search_result_by_endpoint(self, run_with_cookie: str = 'agree_terms'):
        for element in self.page_element.CHARACTERS:
            url = self.page_element.GOOGLE_MAIN_PAGE + 'search?q=' + element
            self.driver.get(url)
            self.driver.execute_script('document.body.style.zoom="50%"')
            self.driver.save_screenshot(
                './logs/images/' + run_with_cookie + '/endpoints/endpoint_?q=' + element + '_log.png')

    def check_unexpected_endpoint(self, run_with_cookie: str = 'agree_terms'):
        for element in self.endpoints:
            url = self.page_element.GOOGLE_MAIN_PAGE + element
            self.driver.get(url)
            self.driver.execute_script('document.body.style.zoom="50%"')
            self.driver.save_screenshot(
                './logs/images/' + run_with_cookie + '/endpoints/unexpected/endpoint_?q=' + element + '_log.png')
