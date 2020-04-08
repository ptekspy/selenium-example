# Scraping any url with selenium firefox browser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def getSoup(url, browser):
    browser.get(url)
    soup = BeautifulSoup(browser.page_source, "html.parser")
    return soup


if __name__ == "__main__":
    url = "https://www.amazon.in/Automate-Boring-Stuff-Python-Programming-ebook/dp/B00WJ049VU"
    options = Options()
    # Uncomment to make browser run in background
    options.add_argument("--headless")
    browser = webdriver.Firefox(options=options)
    try:
        soup = getSoup(url, browser)
        elems = soup.select('#buybox > div > table > tbody > tr.kindle-price > td.a-color-price.a-size-medium.a-align-bottom '
                    '> span')
        # to get the price without any whitespace:
        elems_stripped = []
        for elem in elems:
            elems_stripped.append(elem.get_text().strip())
        print(elems_stripped)
        # Make sure to close the browser
        # Especially if running "headless"
        browser.quit()
    except Exception as ex:
        print(ex)
        browser.quit()
