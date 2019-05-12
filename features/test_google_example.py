from pages.google_page import GooglePage


def test_google_search(driver):
    google_page = GooglePage(driver, "https://google.com")
    google_page.go_to_page()
    google_page.fill_search("selenium")
    google_page.click_search()
    assert google_page.get_title() == "selenium - Google Search"
