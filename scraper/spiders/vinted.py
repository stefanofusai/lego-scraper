import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class VintedSpider(BaseSpider):
    name = "vinted"

    allowed_domains = ["vinted.it"]
    start_urls = [
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40539&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40623&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40624&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40625&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40626&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75280&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75300&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75301&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75323&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75324&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75337&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75342&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75343&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75347&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        # "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75979&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=lego+star+wars&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=1,6&order=newest_first",
    ]

    def start_requests(self):
        yield scrapy.Request(
            "https://www.vinted.it/catalog", callback=self._start_requests
        )

    def _start_requests(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        for result in response.json()["items"]:
            yield Item(
                site="Vinted",
                id=result["id"],
                url=result["url"],
                image=result["photo"]["url"],
                title=result["title"],
                currency="€",
                price=float(result["price"]),
                condition=None,
            )

        if len(response.json()["items"]) > 0:
            page_curr = int(response.url.split("page=")[1].split("&")[0])
            yield scrapy.Request(
                response.url.replace(f"page={page_curr}", f"page={page_curr+1}"),
                callback=self.parse,
            )
