from scraper.items import Item
from scraper.spiders.base import BaseSpider


class CossutoSpider(BaseSpider):
    name = "cossuto"

    allowed_domains = ["cossuto.it"]
    start_urls = [
        "https://cossuto.it/instantSearchFor?q=lego+40539",
        "https://cossuto.it/instantSearchFor?q=lego+40615",
        "https://cossuto.it/instantSearchFor?q=lego+40623",
        "https://cossuto.it/instantSearchFor?q=lego+40624",
        "https://cossuto.it/instantSearchFor?q=lego+40625",
        "https://cossuto.it/instantSearchFor?q=lego+40626",
        "https://cossuto.it/instantSearchFor?q=lego+75290",
        "https://cossuto.it/instantSearchFor?q=lego+75300",
        "https://cossuto.it/instantSearchFor?q=lego+75301",
        "https://cossuto.it/instantSearchFor?q=lego+75304",
        "https://cossuto.it/instantSearchFor?q=lego+75312",
        "https://cossuto.it/instantSearchFor?q=lego+75320",
        "https://cossuto.it/instantSearchFor?q=lego+75323",
        "https://cossuto.it/instantSearchFor?q=lego+75324",
        "https://cossuto.it/instantSearchFor?q=lego+75327",
        "https://cossuto.it/instantSearchFor?q=lego+75329",
        "https://cossuto.it/instantSearchFor?q=lego+75330",
        "https://cossuto.it/instantSearchFor?q=lego+75333",
        "https://cossuto.it/instantSearchFor?q=lego+75336",
        "https://cossuto.it/instantSearchFor?q=lego+75342",
        "https://cossuto.it/instantSearchFor?q=lego+75345",
        "https://cossuto.it/instantSearchFor?q=lego+75347",
        "https://cossuto.it/instantSearchFor?q=lego+75348",
        "https://cossuto.it/instantSearchFor?q=lego+75350",
        "https://cossuto.it/instantSearchFor?q=lego+75351",
        "https://cossuto.it/instantSearchFor?q=lego+75352",
        "https://cossuto.it/instantSearchFor?q=lego+75353",
        "https://cossuto.it/instantSearchFor?q=lego+75354",
        "https://cossuto.it/instantSearchFor?q=lego+75356",
        "https://cossuto.it/instantSearchFor?q=lego+75359",
        "https://cossuto.it/instantSearchFor?q=lego+75360",
        "https://cossuto.it/instantSearchFor?q=lego+75361",
        "https://cossuto.it/instantSearchFor?q=lego+75364",
        "https://cossuto.it/instantSearchFor?q=lego+75369",
    ]

    def parse(self, response):
        try:
            result = response.json()["Products"][0]

        except IndexError:
            return

        yield Item(
            site="Cossuto",
            id=result["Id"],
            url=f"https://cossuto.it{result['CustomProperties']['Url']}",
            image=result["DefaultPictureModel"]["FullSizeImageUrl"],
            title=result["Name"],
            currency="€",
            price=result["ProductPrice"]["PriceValue"],
            condition=None,
            in_stock=not result["ProductPrice"]["DisableBuyButton"],
        )
