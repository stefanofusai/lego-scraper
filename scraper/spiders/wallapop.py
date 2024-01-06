import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class WallapopSpider(BaseSpider):
    name = "wallapop"

    allowed_domains = ["wallapop.com"]
    start_urls = [
        "https://api.wallapop.com/api/v3/general/search?keywords=lego+star+wars&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
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
            )

        if len(results) > 0:
            offset_curr = int(response.url.split("&start=")[1].split("&")[0])
            print(
                response.url.replace(
                    f"&start={offset_curr}", f"&start={offset_curr+40}"
                ).replace(
                    f"&items_count={offset_curr}", f"&items_count={offset_curr+40}"
                )
            )
            yield scrapy.Request(
                response.url.replace(
                    f"&start={offset_curr}", f"&start={offset_curr+40}"
                ).replace(
                    f"&items_count={offset_curr}", f"&items_count={offset_curr+40}"
                ),
                callback=self.parse,
            )
