import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadoLivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/veiculos/carros-caminhonetes/_PriceRange_0-30000#deal_print_id=15305460-574a-11ef-ad11-a712f18a7007"]

    page_count = 1
    max_pages = 10

    def parse(self, response):
        products = response.css('div.ui-search-result__content')

        for product in products:
            
            conditions_source = product.css('li.ui-search-card-attributes__attribute::text').getall()
            history = product.css('span.ui-pb-label::text').getall()

            try:
                yield {
                    'is_checked': product.css('label.ui-search-styled-label.ui-search-item__highlight-label__text::text').get(),
                    'money_amount': product.css('span.andes-money-amount__fraction::text').get(),
                    'name': product.css('h2.ui-search-item__title::text').get(),
                    'year': conditions_source[0] if len(conditions_source) > 0 else None,
                    'km': conditions_source[1] if len(conditions_source) > 1 else None,
                    'is_history': history[0] if len(history[0]) > 0 else None,
                    'location': product.css('span.ui-search-item__group__element.ui-search-item__location::text').get(),
                }
            except:
                continue
        
        if self.page_count < self.max_pages:
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)