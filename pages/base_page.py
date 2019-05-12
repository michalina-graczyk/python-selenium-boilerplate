from urllib.parse import urljoin
from pages.page_object import PageObject


class BasePage(PageObject):
    path = "/"

    def __init__(self, driver, base_url):
        super().__init__(driver)
        self.base_url = base_url

    def get_page_url(self):
        return urljoin(self.base_url, self.path)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def go_to_page(self):
        self.driver.get(self.get_page_url())
