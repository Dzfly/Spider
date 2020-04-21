import scrapy
import re
import json


# 定义网络爬虫类
class ItcastSpider(scrapy.Spider):
    # 每个爬虫必须要有一个名字
    name = "test"
    heads = {
        "Accept": "* / *",
        "Accept - Encoding": "gzip, deflate, br",
        "Accept - Language": "zh - CN, zh; q = 0.9",
        "Connection": "keep - alive",
        "Host": "club.jd.com",
        "Referer": "https: // item.jd.com / 100011336064.html",
        "Sec - Fetch - Dest": "script",
        "Sec - Fetch - Mode": "no - cors",
        "Sec - Fetch - Site": "same - site",
        "User - Agent": "Mozilla / 5.0(Windows NT 10.0; WOW64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 81.0.4044.92 Safari / 537.36",
    }
    url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98&productId=100011336064&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1"

    # 入口方法，当爬虫启动后会先执行这个方法
    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.heads, callback=self.parse)

    def parse(self, response):
        print(response.text)
        # 正则表达式，贪婪匹配
        # 匹配()中间的内容
        p = re.compile(r'[(](.*)[)]', re.S)
        # 匹配后返回一个数组
        r = re.findall(p, response.text)
        jsonstr = r[0]
        # 将json字符串转化成json对象
        jsonobj = json.loads(jsonstr)
        for line in jsonobj["comments"]:
            id = line["id"]
            nickname = line["nickname"]
            productColor = line["productColor"]
            productSize = line["productSize"]
            print("%s\t%s\t%s\t%s" % (id, nickname, productColor, productSize))
