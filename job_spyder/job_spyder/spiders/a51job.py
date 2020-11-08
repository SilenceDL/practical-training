import scrapy
from job_spyder.items import JobSpyderItem
from scrapy.http import Request

class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['https://www.51job.com']
    start_urls = ['https://jobs.51job.com/baoding/p1/']

    def parse(self, response):
        pages = response.xpath('//input[@id="hidTotalPage"]/@value').extract()[0]
        pages = int(pages)
        # print("\n The Page is %d \n" %pages)
        for p in range(1, pages + 1):
            # print("第 %d 页 \n" %p)
            yield Request("https://jobs.51job.com/chongqing/baoding/p" + str(p), callback=self.parsecontent,dont_filter=True)

    def parsecontent(self, response):
        contents = response.xpath('//p[@class="info"]')
        for content in contents:
            item = JobSpyderItem()
            item['title'] = content.xpath('span/a/@title').extract_first('').strip()
            item['company'] = content.xpath('a/@title').extract_first('').strip()
            pays = content.xpath('span[@class="location"]/text()').extract_first('').strip()
            if not pays:
                pays = '面议'
            item['salary'] = pays
            item['location'] = content.xpath('span[@class="location name"]/text()').extract_first('').strip()
            pushdate = content.xpath('span[@class="time"]/text()').extract_first('').strip()
            pushdate = "2020-" + pushdate
            item['date'] = pushdate
            item['datasource'] = '51Job'

            yield item