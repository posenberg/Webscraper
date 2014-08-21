
from living_social.items import LivingSocialDeal

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.loader import XPathItemLoader
from scrapy.contrib.loader.processor import Join, MapCompose

class LivingSocialSpider(BaseSpider):
    name = "livingsocial"
    allowed_domains = ["livingsocial.com"]
    start_urls = ["http://www.livingsocial.com/cities/15-san-francisco"]

    deals_list_xpath = '//li[@dealid]' #between <li dealid=" "></li>
    item_fields = {'title': './/a/div[@class="deal-details"]/h2[@itemprop]/text()',
                   'link': './/a/@href',
                   'description': './/a/div[@class="deal-details"]/p/text()',
                   'category': './/a/div[@class="deal-image"]/p[@class="deal-category"]/text()',
                   'location': './/a/div[@class="deal-details"]/p[@class="location"]/text()',
                   'original_price': './/a/div[@class="deal-gem-prices"]/span[@class="deal-strikethrough-price"]/text()',
                   'price': './/a/div[@class="deal-gem-prices"]/span[@class="deal-price"]/text()'}

    def parse(self, response):
        """
        Default callback used by Scrapy to process downloaded responses

        Testing contracts:
        @url http://www.livingsocial.com/cities/15-san-francisco
        @returns items 1
        @scrapes title link

        """
        selector = HtmlXPathSelector(response)

        # iterate over deals
        for deal in selector.select(self.deals_list_xpath):
            loader = XPathItemLoader(LivingSocialDeal(), selector=deal)

            # define processors
            loader.default_input_processor = MapCompose(unicode.strip)
            loader.default_output_processor = Join()

            # iterate over fields and add xpaths to the loader
            for field, xpath in self.item_fields.iteritems():
                loader.add_xpath(field, xpath)
            yield loader.load_item()