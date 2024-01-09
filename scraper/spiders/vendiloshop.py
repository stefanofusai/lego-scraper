from scrapy.http import FormRequest

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class VendiloShopSpider(BaseSpider):
    name = "vendiloshop"

    allowed_domains = ["sniperfast.com"]
    start_urls = [
        "40539",
        "40615",
        "40623",
        "40624",
        "40625",
        "40626",
        "75290",
        "75300",
        "75301",
        "75304",
        "75312",
        "75320",
        "75323",
        "75324",
        "75327",
        "75329",
        "75330",
        "75333",
        "75336",
        "75342",
        "75345",
        "75347",
        "75348",
        "75350",
        "75351",
        "75352",
        "75353",
        "75354",
        "75356",
        "75359",
        "75360",
        "75361",
        "75364",
        "75369",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield FormRequest(
                "https://api.sniperfast.com/search",
                formdata={
                    "key": "26d868-4d8dda-4d40ea-d98082-9a6c33",
                    "name": "index_vndshp",
                    "sort": "rel",
                    "sort_num": "100",
                    "sort_page": "1",
                    "input[user_input]": url,
                    "input[cat1]": "",
                    "input[cat2]": "",
                    "input[cat3]": "",
                    "input[cat4]": "",
                    "filters[manufacturer]": "",
                    "filters[manufacturer_count]": "10",
                    "filters[price][min]": "0",
                    "filters[price][max]": "0",
                    "filters[price][low]": "",
                    "filters[price][high]": "",
                    "last_change": "",
                    "customer": "0_1",
                    "apiv": "2",
                    "sniper_session": "t9s67nf8jnrdtg8bobt2hjud6s",
                },
                callback=self.parse,
                cb_kwargs={"url": url},
            )

    def parse(self, response, url):
        try:
            for result in response.json()["result"]:
                if url in result["name"][0]:
                    break

            else:
                return

        except KeyError:
            return

        yield Item(
            site="Vendilo Shop",
            id=result["id"],
            url=result["url"],
            image=result["img"],
            title=result["name"][0],
            currency="€",
            price=float(result["price"].replace(",", ".")),
            condition=None,
            in_stock=result["quantity"] > 0,
        )
