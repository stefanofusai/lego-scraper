import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class WallapopSpider(BaseSpider):
    name = "wallapop"

    allowed_domains = ["wallapop.com"]
    start_urls = [
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+40539&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+40615&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+40623&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+40624&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+40625&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+40626&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75290&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75300&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75301&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75304&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75312&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75320&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75323&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75324&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75327&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75329&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75330&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75333&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75336&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75342&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75345&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75347&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75348&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75350&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75351&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75352&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75353&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75354&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75356&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75359&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75360&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75361&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75364&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+75369&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
    ]

    def parse(self, response):
        results = response.json()["search_objects"]

        for result in results:
            yield Item(
                site="Wallapop",
                id=result["id"],
                url=f"https://it.wallapop.com/item/{result['web_slug']}",
                image=result["images"][0]["xlarge"],
                title=result["title"],
                currency="€",
                price=result["price"],
                condition=None,
                in_stock=True,
            )

        if len(results) > 0:
            offset_curr = int(response.url.split("&start=")[1].split("&")[0])
            yield scrapy.Request(
                response.url.replace(
                    f"&start={offset_curr}", f"&start={offset_curr+40}"
                ).replace(
                    f"&items_count={offset_curr}", f"&items_count={offset_curr+40}"
                ),
                callback=self.parse,
            )
