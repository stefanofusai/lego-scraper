from scraper.items import SubitoItem
from scraper.pipelines import SubitoPipeline
from scraper.spiders.base import BaseSpider


class SubitoSpider(BaseSpider):
    name = "subito"

    allowed_domains = ["subito.it"]
    custom_settings = {"ITEM_PIPELINES": {SubitoPipeline: 100}}
    start_urls = [
        "https://www.subito.it/hades/v1/search/items?q=40539&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=40623&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=40624&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=40625&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=40626&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75280&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75300&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75301&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75323&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75324&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75337&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75342&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75343&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75347&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=75979&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
        "https://www.subito.it/hades/v1/search/items?q=lego+star+wars&c=21&t=s&qso=false&shp=true&urg=false&sort=datedesc&lim=100&start=0&ic=10,20",
    ]

    def parse(self, response):
        for item in response.json()["ads"]:
            yield SubitoItem(
                urn=item["urn"],
                type=item["type"],
                category=item["category"],
                subject=item["subject"],
                body=item["body"],
                dates=item["dates"],
                images=item["images"],
                images_360=item["images_360"],
                features=item["features"],
                advertiser=item["advertiser"],
                geo=item["geo"],
                urls=item["urls"],
            )
