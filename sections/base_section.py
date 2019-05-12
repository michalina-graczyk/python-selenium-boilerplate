from selenium.webdriver.common.by import By
from pages.page_object import PageObject


class BaseSection(PageObject):
    def __init__(self, driver, css_selector):
        super().__init__(driver)
        self.css_selector = css_selector

    def is_visible(self):
        element = self.driver.find_element(By.CSS_SELECTOR, self.css_selector)
        return element.is_displayed()
