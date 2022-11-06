import pytest


from action.InputCharacters import InputCharacters
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class TestEndpointWithAgree:

    # def __init__(self):
    #     self.input_characters = InputCharacters(self.driver)

    def test_search_result_by_endpoint(self):
        input_characters = InputCharacters(self.driver)
        input_characters.select_google_terms('y')
        input_characters.check_search_result_by_endpoint()
