import scrapy
from bs4 import BeautifulSoup
from lxml import etree
import js2xml


class Spider(scrapy.Spider):
    name = "test4"
    heads = {

    }
    url = "https://item.jd.com/100011351652.html"

    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.heads, callback=self.parse)

    def parse(self, response):
        # html --> xml对象
        soup = BeautifulSoup(response.text, 'lxml')
        # 选择script标签
        src = soup.select("html head script")[0].string
        # js代码 --> xml文档对象
        src_text = js2xml.parse(src, debug=False)
        src_tree = js2xml.pretty_print(src_text)
        # xml文档对象 --> html文档对象
        selector = etree.HTML(src_tree)

        # 使用html xpath查找标签
        value = selector.xpath("//property[@name = 'skuId']/number/@value")
        print(value)

        for obj in selector.xpath("//property[@name = 'colorSize']/array/object"):
            # @value 获取标签属性的值
            # ./ 从当前标签开始寻址
            id = obj.xpath("./property/number/@value")[0]
            str = ",".join(obj.xpath("./property/string/text()"))
            print(id)
            print(str)
