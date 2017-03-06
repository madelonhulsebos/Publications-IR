import scrapy


class MethodsSpider(scrapy.Spider):
    name = "methods"
    start_urls = [
        "https://en.wikipedia.org/wiki/List_of_machine_learning_concepts",
    ]

    def parse(self, response):
        # page = response.url.split("/")[-2]
        # filename = 'methods-%s.html' % page
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for method in response.css("li"):
            yield {
                'title': method.css("a::attr(title)").extract_first(),
            }

            # response.css("li a span.toctext::text").extract_first()
            # returns u'Supervised learning'

            # response.css("li a::attr(title)").extract_first()
            # returns u'AODE'
