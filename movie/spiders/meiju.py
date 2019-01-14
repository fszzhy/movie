# -*- coding: utf-8 -*-
import scrapy
from movie .items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'  # 爬虫名。一个项目下可能有多个爬虫，并且每个爬虫有优先级，并发等设置
    allowed_domains = ['meijutt.com']  # 为了防止爬虫项目自动爬取到其它网站，设置限制，每一次请求前都会检查请求的网址是否属于这个域名下，实对话才允许请求，注意： 爬取日志爬取网址后响应总为None,检查allowed_domain 书写是否正确，值的一级域名。
    start_urls = ['http://www.meijutt.com/new100.html']  # 第一个请求的uil，整个程序逻辑的入口，得到的response返回给 self,response=response

    def parse(self, response):
        # print(response.status_codes,response.cntent,response.text)
        # lxml.HTML(response.text)  : dom.xpath('')
        # Selector (response.text).xpath('').extract
        # 获取剧集名
        movies_list = response.xpath('//ul[@class="top-list  fn-clear"]/li')# [<li>对象，<li>对象]
        for movie in  movies_list:
            # movie .xpath (('./h5/text()').extratact()  # xpath()返回
            # xpath()
            name = movie.xpath('./h5/a/text()').extract_first()

            item = MovieItem()
            item['name']= name  # item['name']  # name
            yield item  # 相当于同步脚本方法中的return

