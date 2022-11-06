# import pytest
#
# from action.LinkOnClick import LinkOnClick
# from action.SelectTerms import SelectTerms
#
#
# @pytest.mark.usefixtures("setup")
# class TestGooglePageLinks:
#
#     def test_available_links(self):
#         SelectTerms(self.driver).select_google_terms('y')
#         link_on_click = LinkOnClick(self.driver)
#         link_on_click.click_all_links_on_main_page()
