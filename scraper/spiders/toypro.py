from scraper.items import Item
from scraper.spiders.base import BaseSpider


class ToyProSpider(BaseSpider):
    name = "toypro"

    allowed_domains = ["toypro.com"]
    start_urls = [
        "https://www.toypro.com/it/product/42307/taverna-mos-eisley",
        "https://www.toypro.com/it/product/41832/imperial-tie-fighter",
        "https://www.toypro.com/it/product/41833/x-wing-fighter-di-luke-skywalker",
        "https://www.toypro.com/it/product/41835/darth-vadertm-helmet",
        "https://www.toypro.com/it/product/42911/boba-fetts-starship-75312",
        "https://www.toypro.com/it/product/45246/lego-snowtrooper-battle-pack",
        "https://www.toypro.com/it/product/46967/the-justifier",
        "https://www.toypro.com/it/product/45245/lego-lattacco-del-dark-trooper",
        "https://www.toypro.com/it/product/45248/lego-casco-di-luke-skywalker-red-five",
        "https://www.toypro.com/it/product/45250/diorama-volo-sulla-trincea-della-morte-nera",
        "https://www.toypro.com/it/product/45251/addestramento-jedi-su-dagobah-diorama",
        "https://www.toypro.com/it/product/46969/jedi-starfighter-di-obi-wan-kenobi",
        "https://www.toypro.com/it/product/46972/trasporto-dell-inquisitore-scythe",
        "https://www.toypro.com/it/product/49334/battle-pack-clone-trooper-legione-501",
        "https://www.toypro.com/it/product/49336/lego-tie-bomber",
        "https://www.toypro.com/it/product/49337/fang-fighter-mandaloriano-vs-tie-interceptor",
        "https://www.toypro.com/it/product/49339/casco-del-comandante-clone-cody",
        "https://www.toypro.com/it/product/49340/diorama-della-sala-del-trono-dell-imperatore",
        "https://www.toypro.com/it/product/49341/diorama-dell-inseguimento-dello-speeder-di-endor",
        "https://www.toypro.com/it/product/50551/battle-pack-clone-trooper-della-332a-compagnia-di-ahsoka",
        "https://www.toypro.com/it/product/50552/jedi-starfighter-di-yoda",
        "https://www.toypro.com/it/product/50555/nuova-repubblica-e-wing-contro-il-caccia-stellare-di-shin-hati",
        "https://www.toypro.com/it/product/50558/mech-di-boba-fett",
    ]

    def parse(self, response):
        yield Item(
            site="ToyPro",
            id=response.text.split('item_id: "')[1].split('"')[0],
            url=response.url,
            # <img class="c_product-top__image" src="https://cdn.toypro.com/media/cache/tp_product_detail/uploads/images/custom/41832-src.webp" alt="LEGO&reg; 75300 Imperial TIE Fighter">
            image=response.css("img.c_product-top__image::attr(src)").get(),
            title=response.css("meta[property='og:title']::attr(content)").get(),
            currency="€",
            price=float(response.text.split("price: ")[1].split(",")[0]),
            condition=None,
            in_stock="https://schema.org/InStock" in response.text,
        )
