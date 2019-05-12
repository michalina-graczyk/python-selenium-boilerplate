from selenium import webdriver
from bin.driver_path import get_driver_path


def get_browser_options(browser_name, is_headless):
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()

    if is_headless:
        options.add_argument("headless")

    options.add_argument("window-size=1200x600")
    return options


def get_chrome_driver(is_headless):
    options = get_browser_options("chrome", is_headless)
    driver_path = get_driver_path("chrome")
    chrome_driver = webdriver.Chrome(
        executable_path=driver_path, options=options)
    return chrome_driver


def get_firefox_driver(is_headless):
    options = get_browser_options("firefox", is_headless)
    driver_path = get_driver_path("firefox")
    firefox_driver = webdriver.Firefox(
        executable_path=driver_path, options=options)
    return firefox_driver


def get_driver(browser_name, is_headless):
    if browser_name == "chrome":
        return get_chrome_driver(is_headless)
    elif browser_name == "firefox":
        return get_firefox_driver(is_headless)
