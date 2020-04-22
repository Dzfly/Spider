# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CommentPipeline(object):
    # 初始化函数，一般用作建立数据库连接
    def __init__(self):
        pass

    # 输出处理方法
    def process_item(self, item, spider):
        print(item['id'], item['nickname'])
