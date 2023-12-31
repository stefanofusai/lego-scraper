import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class SubitoSpider(BaseSpider):
    name = "subito"

    allowed_domains = ["subito.it"]
    start_urls = [
        "https://www.subito.it/hades/v1/search/items?q=lego+40539&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+40615&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+40623&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+40624&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+40625&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+40626&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75290&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75300&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75301&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75304&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75312&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75320&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75323&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75324&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75327&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75329&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75330&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75333&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75336&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75342&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75345&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75347&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75348&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75350&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75351&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75352&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75353&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75354&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75356&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75359&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75360&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75361&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75364&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
        "https://www.subito.it/hades/v1/search/items?q=lego+75369&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0",
    ]

    def parse(self, response):
        results = response.json()["ads"]

        for result in results:
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
                site="Subito",
                id=result["urn"],
                url=result["urls"]["default"],
                image=image,
                title=result["subject"],
                currency="€",
                price=float(price.replace(" €", "")),
                condition=condition,
                in_stock=True,
            )

        if len(results) > 0:
            offset_curr = int(response.url.split("&start=")[1].split("&")[0])
            yield scrapy.Request(
                response.url.replace(
                    f"&start={offset_curr}", f"&start={offset_curr+100}"
                ),
                callback=self.parse,
            )
