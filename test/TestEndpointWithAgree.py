import pytest

from action.InputCharacters import InputCharacters
from selenium import webdriver

from action.SearchEndpoint import SearchEndpoint
from action.SelectTerms import SelectTerms


@pytest.mark.usefixtures("setup")
class TestEndpointWithAgree:

    # def __init__(self):
    #     self.input_characters = InputCharacters(self.driver)

    def test_search_result_by_endpoint(self):
        search_endpoint = SearchEndpoint(self.driver)
        SelectTerms(self.driver).select_google_terms('n')
        search_endpoint.check_search_result_by_endpoint('agree_terms')
        search_endpoint.check_unexpected_endpoint()
