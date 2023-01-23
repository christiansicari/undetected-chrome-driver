import undetected_chromedriver as uc
from bs4 import BeautifulSoup
def main(args=None):
    driver = uc.Chrome()
    driver.get("https://www.google.com")
    title = driver.title
    print(title)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    div = soup.findAll('div')
    print(div)
    driver.quit()


if __name__ == "__main__":
    import argparse
    main()