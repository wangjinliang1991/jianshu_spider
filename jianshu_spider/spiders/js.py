# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItem

class JsSpider(CrawlSpider):
    name = 'js'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/']

    rules = (
        Rule(LinkExtractor(allow=r'.*/p/[0-9a-z]{12}.*'), callback='parse_detail', follow=True),
    )

    def parse_detail(self, response):
        title = response.xpath('//div[@class="article"]/h1/text()').get()
        avatar = response.xpath('//div[@class="article"]//a[@class="avatar"]/img/@src').get()
        author = response.xpath('//div[@class="author"]//span[@class="name"]/a/text()').get()
        pub_time = response.xpath('//span[@class="publish-time"]/text()').get().replace("*","")
        url1 = response.url
        url2 = url1.split("?")[0]
        article_id = url2.split('/')[-1]
        content = response.xpath('//div[@class="show-content"]').get()
        word_count = response.xpath('//span[@class="wordage"]/text()').get()
        comment_count = response.xpath('//span[@class="comments-count"]/text()').get()
        like_count = response.xpath('//span[@class="likes-count"]/text()').get()
        read_count = response.xpath('//span[@class="views-count"]/text()').get()

        subjects = ','.join(response.xpath('//div[@class="include-collection"]/a/div/text()').getall())

        item = ArticleItem(
            title=title,
            avatar=avatar,
            author=author,
            article_id=article_id,
            origin_url=response.url,
            content = content,
            pub_time=pub_time,
            word_count=word_count,
            comment_count=comment_count,
            read_count=read_count,
            like_count=like_count
        )
        yield item