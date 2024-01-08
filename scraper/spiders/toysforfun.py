from scraper.items import Item
from scraper.spiders.base import BaseSpider


class ToysForFunSpider(BaseSpider):
    name = "toysforfun"

    allowed_domains = ["toys-for-fun.com"]
    start_urls = [
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+40539&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+40615&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+40623&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+40624&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+40625&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+40626&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75290&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75300&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75301&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75304&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75312&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75320&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75323&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75324&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75327&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75329&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75330&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75333&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75336&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75342&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75345&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75347&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75348&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75350&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75351&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75352&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75353&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75354&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75356&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75359&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75360&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75361&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75364&__store=de",
        "https://www.toys-for-fun.com/de/search/ajax/suggest/?q=lego+75369&__store=de",
    ]

    def parse(self, response):
        try:
            result = response.json()[-1]

        except IndexError:
            return

        if "entity_id" not in result:
            return

        yield Item(
            site="Toys for Fun",
            id=result["entity_id"],
            url=f"https://www.toys-for-fun.com/de/{result['url']}",
            image=f"https://www.toys-for-fun.com/de/{result['thumbnail']}",
            title=result["name"][0],
            currency="€",
            price=result["price"][0]["final_price"],
            condition=None,
            in_stock=result["stock"]["is_in_stock"],
        )
