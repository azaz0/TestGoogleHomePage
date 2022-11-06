import pytest

from LoggerHandler import LoggerHandler
from action.InputCharacters import InputCharacters
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class TestUserInputCharactersWithAgree:

    # def __init__(self):
    #     self.input_characters = InputCharacters(self.driver)

    def test_search_result_with_decline(self):
        input_characters = InputCharacters(self.driver)
        input_characters.select_google_terms('n')
        results = input_characters.check_search_result()



