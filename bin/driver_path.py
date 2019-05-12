import os


def get_driver_path(browser_name):
    project_root = os.path.abspath(os.path.dirname(__file__))
    driver_path = os.path.join(project_root, browser_name + "driver")
    return driver_path
