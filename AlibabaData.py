from bs4 import BeautifulSoup
from selenium import webdriver

# Provide the search address of any products in Alibaba site
ALIBABA_WEBSITE = 'https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.the-new-header_fy23_pc_search_bar.keydown__Enter&tab=all&SearchText=tape'

driver = webdriver.Chrome()
driver.get(ALIBABA_WEBSITE)
html_page_source = driver.page_source


class AlibabaData:
    def __init__(self):
        self.html = BeautifulSoup(html_page_source, "html.parser")
        self.name = []
        self.price = []
        self.min_qty = []
        self.link = []

    def get_data(self):
        all_products = self.html.find_all(name="div", class_="list-card-layout__info")
        self.name = [name.find(name="span").text for name in all_products]
        self.price = [price.find(name="div", class_="search-card-e-price-main").text for price in all_products]
        self.min_qty = [qty.find_all(name="div", class_="search-card-m-sale-features__item")[1].text for qty in
                        all_products]
        self.link = [link.find(name="a").get("href").split("//")[1] for link in all_products]

        return [self.name, self.price, self.min_qty, self.link]
