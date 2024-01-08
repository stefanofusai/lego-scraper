from scraper.items import Item
from scraper.spiders.base import BaseSpider


class DisneySpider(BaseSpider):
    name = "disney"

    allowed_domains = ["shopdisney.it"]
    start_urls = [
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461031848939",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461031897364",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461031897449",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461031935066",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461032361154",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461032775494",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461033557662",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461032775562",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461032775647",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461032998572",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461032998657",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461033557907",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461033557822",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461032998817",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461034028246",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461034028659",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=417167274937",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461034183822",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=461034183907",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=417167275439",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=417167275279",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=417167459662",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=417167275507",
        "https://www.shopdisney.it/on/demandware.store/Sites-shopDisneyIT-Site/it_IT/Product-Variation?pid=417167454049",
    ]

    def parse(self, response):
        result = response.json()["product"]
        yield Item(
            site="Disney",
            id=result["id"],
            url=f"https://www.shopdisney.it{result['selectedProductUrl']}",
            image=result["images"]["large"][0]["url"],
            title=result["productName"],
            currency="€",
            price=result["price"]["selling"]["value"],
            condition=None,
            in_stock=result["available"],
        )
