import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class SubitoSpider(BaseSpider):
    name = "subito"

    allowed_domains = ["subito.it"]
    start_urls = [
        # "https://www.subito.it/hades/v1/search/items?q=40539&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=40623&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=40624&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=40625&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=40626&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75280&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75300&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75301&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75323&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75324&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75337&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75342&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75343&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75347&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        # "https://www.subito.it/hades/v1/search/items?q=75979&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=lego+star+wars&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
    ]

    def parse(self, response):
        for result in response.json()["ads"]:
            try:
                image = result["images"][0]["scale"][-1]["uri"]

            except IndexError:
                image = None

            try:
                price = [x for x in result["features"] if x["label"] == "Prezzo"][0][
                    "values"
                ][0]["value"]

            except IndexError:
                continue

            try:
                condition = [
                    x for x in result["features"] if x["label"] == "Condizione"
                ][0]["values"][0]["value"]

            except IndexError:
                condition = None

            yield Item(
                site="Subito.it",
                id=result["urn"],
                url=result["urls"]["default"],
                image=image,
                title=result["subject"],
                currency="€",
                price=float(price.replace(" €", "")),
                condition=condition,
            )

        if len(response.json()["ads"]) > 0:
            offset_curr = int(response.url.split("start=")[1].split("&")[0])
            yield scrapy.Request(
                response.url.replace(
                    f"start={offset_curr}", f"start={offset_curr+100}"
                ),
                callback=self.parse,
            )
