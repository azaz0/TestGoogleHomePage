class PageElement:
    SEARCH_BAR = '//input[@name="q"]'
    SEARCH_BUTTON = '//input[@class="gNO89b"]'
    RESULT_TEXT = '//h3[@class="LC20lb MBeuO DKV0Md"]'
    CHARACTERS = ['""', "''", '\'', '\"',
                  '(', ')', '*', '&', '^',
                  '$', '%', '#', '@', '!',
                  '?', ',', ';', ':', '{',
                  '}', '>', '<', '/', '\\',
                  '1', '2', '3', '4', '5',
                  '6', '7', '8', '9', 'S',
                  '|', '-', '+', '_', '=',
                  'google']
    GOOGLE_MAIN_PAGE = 'https://www.google.pl/'
    LUCKY_BUTTON = '//input[@class="RNmpXc"]'
    LINKS = '//a[not(@class="gb_A")]'
