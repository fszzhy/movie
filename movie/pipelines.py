# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


# 管道： 数据清洗，去重
# 持久化： 写txt。csv。写入数据库。

# scrapy框架将爬取spider模块和处理层pipeline分离开，使得程序更容易扩展
# spider yield生成的item会交给pipline处理，如果爬取速度和处理速度不一致的话scrapy框架会自动调节。
# spider yield相当于

class MoviePipeline(object):
    def process_item(self, item, spider):
        # 爬虫部分在for循环中yield itemg
        with open('my_meiju.txt','a',encoding='utf-8')as f:
            f.write(str(item['name'])+ '\n')
        return item
