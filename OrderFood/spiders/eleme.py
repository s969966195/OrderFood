# coding=utf-8
import time
import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from OrderFood.items import ElemeItem


def execute_times(driver, times):
    for i in range(times+1):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)


class ElemeSpider(scrapy.Spider):
    name = "eleme"
    allowed_domains = ["ele.me"]
    start_urls = [
        "https://www.ele.me/place/wtw6hgtgmq3v?latitude=31.308881&longitude=121.505927",
    ]

    def parse(self, response):
        driver = webdriver.Chrome()
        driver.get(self.start_urls[0])

        element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//div[@class="place-rstbox clearfix"]'))
        execute_times(driver, -1)

        aurl = driver.find_elements_by_xpath('//a[@class="rasblock"]')
        for url in aurl:
            yield scrapy.Request(url.get_attribute("href"),
                    callback=self.parse_dir_contents)

    def parse_dir_contents(self, response):
        item = ElemeItem()
        item['name'] = driver.find_elements_by_xpath('//*[@class="rstblock-title"]')
        item['url'] = []
        aurl = driver.find_elements_by_xpath('//a[@class="rstblock"]')
        for url in aurl:
            item['url'].append(url.get_attribute("href"))
        item['dfee'] = driver.find_elements_by_xpath('//*[@class="rstblock-cost"]')
        item['dtime'] = driver.find_elements_by_xpath('//*[@class="rstblock-logo"]/span')
        print type(item['name'])
        print type(item['url'])

        for i in item['url']:
            print i

        driver.close()

    
