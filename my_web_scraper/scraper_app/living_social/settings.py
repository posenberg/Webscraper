# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['living_social.spiders']

ITEM_PIPELINES = ['living_social.pipelines.LivingSocialPipeline']

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': '<your username>', # fill in your username here
            'password': '<your postgresql password', # fill in your password here
            'database': 'scrape'}
