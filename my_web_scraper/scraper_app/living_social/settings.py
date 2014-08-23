
BOT_NAME = 'tutorial'

SPIDER_MODULES = ['living_social.spiders']

ITEM_PIPELINES = ['living_social.pipelines.LivingSocialPipeline']

DATABASE = {'drivername': 'postgres',
            'host': 'localhost',
            'port': '5432',
            'username': '<your username>', # fill in your username here
            'password': '<your postgresql password', # fill in your password here
            'database': 'scrape'}
