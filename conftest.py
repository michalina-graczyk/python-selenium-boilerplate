import pytest
from configuration.web_driver import get_driver


def pytest_addoption(parser):
    # pytest built-in fixture which configures custom arguments
    # to be passed to `pytest` command.
    parser.addoption("--browser", default="chrome",
                     action="store", help="browser driver to be used for testing")
    parser.addoption("--headless", action="store_true",
                     help="driver option to run in headless mode")


@pytest.fixture()
def driver(request):
    # Fixture that prepares webdriver to be used in tests.
    # Allows to use `driver` parameter in test functions.
    is_headless = request.config.getoption("--headless")
    browser_name = request.config.getoption("--browser")

    # here configure selenium driver based on parameters above
    driver = get_driver(browser_name, is_headless)
    # return driver to a test function
    yield driver
    # after test function finishes, close the browser
    driver.quit()
