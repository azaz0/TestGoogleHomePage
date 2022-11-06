import pytest

from action.InputCharacters import InputCharacters
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class TestUserInputCharactersWithAgree:

    # def __init__(self):
    #     self.input_characters = InputCharacters(self.driver)

    def test_search_result_with_agree(self):
        input_characters = InputCharacters(self.driver)
        input_characters.select_google_terms('y')
        count_result = input_characters.check_search_result('sss')
        print("results: ", count_result)
