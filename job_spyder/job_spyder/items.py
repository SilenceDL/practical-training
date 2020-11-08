# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobSpyderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field() #职位
    company = scrapy.Field() # 公司
    desc = scrapy.Field() #职位描述
    salary = scrapy.Field() #薪资
    location = scrapy.Field()  #工作地点
    date = scrapy.Field()  #发布时间
    datasource = scrapy.Field() #消息来源
    experience = scrapy.Field() #工作经验
    education = scrapy.Field() #学历要求

