# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# --DEFAULT CODE--
# class BookScraperPipeline:
#     def process_item(self, item, spider):
#         return item


from pymongo import MongoClient

class BookScraperPipeline:
    def open_spider(self, spider):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['books_database']
        self.collection = self.db['books_collection']

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.collection.insert_one(dict(item))
        return item
