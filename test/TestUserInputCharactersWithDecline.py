import pytest

from LoggerHandler import LoggerHandler
from action.InputCharacters import InputCharacters
from selenium import webdriver


@pytest.mark.usefixtures("setup")
class TestUserInputCharactersWithDecline(LoggerHandler):

    # def __init__(self):
    #     self.input_characters = InputCharacters(self.driver)

    def test_search_result(self):
        input_characters = InputCharacters(self.driver)
        input_characters.select_google_terms('n')
        results = input_characters.check_search_result('decline_terms')
        logger = self.get_logger()
        logger.info(results)
