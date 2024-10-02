import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'http://books.toscrape.com/'
    ]

    def parse(self, response):
        # Select all book articles on the page
        books = response.css('article.product_pod')

        # Loop through each book and extract details
        for book in books:
            title = book.css('h3 a::attr(title)').get()
            price = book.css('p.price_color::text').get()
            availability = book.css('p.instock.availability::text').get(default='').strip()

            # Store the extracted data as a dictionary
            yield {
                'title': title,
                'price': price,
                'availability': availability
            }

        # Follow pagination link if available
        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

#To run the spider, type in terminal : scrapy crawl books -o books.json
