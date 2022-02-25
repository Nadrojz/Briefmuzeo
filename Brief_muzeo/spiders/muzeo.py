import scrapy
from Brief_muzeo.items import PropertiesItem

class MuzeoSpider(scrapy.Spider):
    name = 'muzeo'
    allowed_domains = ['web']
    start_urls = ['https://fr.muzeo.com/reproduction-oeuvre/ours-polaire-semblant-prier-baie-de-churchill-canada/alberto-ghizzi-panizza#Ours-polaire-semblant-prier,-Baie-de...-Alberto-Ghizzi-Panizza']

    def parse(self, response):
        item = PropertiesItem()
        item['title'] = response.xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[1]/h1/span[2]/text()').extract()
        # item['price'] = response.xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div[1]/form/div/div[2]/fieldset/div/div[3]/fieldset/div/div[2]/div[2]/div[2]/text()').extract()
        # item['delay'] = response.xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div/div[1]/div[2]/div/div/div/div/div[1]/div/div/div[1]/form/div/div[7]/div[1]/text()').extract()
        # item['image_url'] = response.xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]').extract()
        url = response.xpath('/html/body/div[1]/div[3]/div/div[3]/div/div/div/div[1]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]').extract()
        listdiv = []
        for x in url:
            items = x.split("<")
            items[5] = items[5].split('"')
            listdiv.append(items[5][1])
        item['image_url'] = listdiv[0]
        return item