from pages.base_page import BasePage


class GooglePage(BasePage):
    path = "/"

    # Page elements
    def get_search_input(self):
        element = self.driver.find_element_by_name("q")
        return element

    def get_search_button(self):
        elements = self.driver.find_elements_by_name("btnK")
        return elements[1]

    def get_autocomplete_search_button(self):
        elements = self.driver.find_elements_by_name("btnK")
        return elements[0]

    # Page operation
    def fill_search(self, text):
        self.get_search_input().send_keys(text)

    def click_search(self):
        self.get_search_button().click()
