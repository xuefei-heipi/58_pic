class BaseFunction(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def xpath_find(self, *loc):
        return self.driver.find_element_by_xpath(*loc)

    def link_text_find(self, *loc):
        return self.driver.find_element_by_link_text(*loc)

    def css_find(self, *loc):
        return self.driver.find_element_by_css_selector(*loc)