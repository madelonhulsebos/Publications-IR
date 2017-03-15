import scrapy

class AlgorithmsSpider(scrapy.Spider):
    name = "algorithms"

    start_urls = ['https://en.wikipedia.org/wiki/List_of_algorithms']

    def parse(self, response):
    	# retrieve the html page
        page = response.url.split("/")[-1]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        for algorithm in response.css('li'):
            yield {
                'title': algorithm.css('a::text').extract_first(),
                # 'title': algorithm.css('a::attr(title)').extract_first(),
            }