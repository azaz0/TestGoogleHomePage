# import time
#
# from selenium.webdriver.common.by import By
# from variables.PageElement import PageElement
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class LinkOnClick:
#
#     def __init__(self, driver):
#         self.page_element = PageElement
#         self.driver = driver
#
#     def click_all_links_on_main_page(self):
#         links = WebDriverWait(self.driver, 10).until(
#             EC.presence_of_all_elements_located((By.XPATH, self.page_element.LINKS)))
#         i = 0
#         for link in links:
#             link.click()
#             self.driver.execute_script('document.body.style.zoom="50%"')
#             self.driver.save_screenshot('./logs/images/links/characters/item_' + str(i) + '_log.png')
#             self.driver.back()
#             i = i + 1
