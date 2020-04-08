# Scraping any url with selenium firefox browser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def getSoup(url, browser):
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    return soup


if __name__ == "__main__":
    url = input(" What URL would you like to scrape?\n")
    options = Options()
    # Uncomment to make browser run in background
    # options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    try:
        soup = getSoup(url, browser)
        print(f"The Title of the websiet is: {soup.title.get_text()}")
        # Make sure to close the browser
        # Especially if running "headless"
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.quit()
