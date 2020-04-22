import scrapy


class Spider(scrapy.Spider):
    name = "test3"
    heads = {

    }
    url = "https://item.jd.com/100011351652.html"

    def start_requests(self):
        yield scrapy.Request(url=self.url, headers=self.heads, callback=self.parse)

    def parse(self, response):
        # / 代表从根节点寻址，// 代表全局查询
        # [@class = 'sku-name'] 过滤条件，对标签上面的属性增加过滤条件
        # text() 获取标签的文本内容
        # xpath 返回的是一个数组
        # extract() 返回Unicode字符串
        name = response.xpath("//div[@class = 'sku-name']/text()")[0].extract()
        print(name)
