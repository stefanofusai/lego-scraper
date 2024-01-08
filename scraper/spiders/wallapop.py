import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class WallapopSpider(BaseSpider):
    name = "wallapop"

    allowed_domains = ["wallapop.com"]
    start_urls = [
        "https://api.wallapop.com/api/v3/general/search?keywords=40539&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=40623&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=40624&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=40625&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=40626&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75300&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75301&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75304&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75312&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75320&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75323&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75324&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75327&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75329&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75330&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75333&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75336&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75342&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75345&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75347&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75348&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75352&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75353&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75356&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75359&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75360&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75361&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=75364&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
        "https://api.wallapop.com/api/v3/general/search?keywords=lego&condition=new,as_good_as_new&start=0&items_count=0&filters_source=quick_filters&order_by=newest&step=0",
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
            yield scrapy.Request(
                response.url.replace(
                    f"&start={offset_curr}", f"&start={offset_curr+40}"
                ).replace(
                    f"&items_count={offset_curr}", f"&items_count={offset_curr+40}"
                ),
                callback=self.parse,
            )
