import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class VintedSpider(BaseSpider):
    name = "vinted"

    allowed_domains = ["vinted.it"]
    start_urls = [
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40539&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40623&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40624&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40625&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=40626&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75300&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75301&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75304&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75312&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75320&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75323&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75324&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75327&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75329&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75330&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75333&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75336&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75342&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75345&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75347&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75348&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75352&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75353&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75356&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75359&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75360&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75361&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
        "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=960&search_text=75364&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=&order=newest_first",
    ]

    def start_requests(self):
        yield scrapy.Request(
            "https://www.vinted.it/catalog", callback=self._start_requests
        )

    def _start_requests(self, response):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        results = response.json()["items"]

        for result in results:
            yield Item(
                site="Vinted",
                id=result["id"],
                url=result["url"],
                image=result["photo"]["url"],
                title=result["title"],
                currency="€",
                price=float(result["price"]),
                condition=None,
                in_stock=True,
            )

        if len(results) > 0:
            page_curr = int(response.url.split("?page=")[1].split("&")[0])
            yield scrapy.Request(
                response.url.replace(f"?page={page_curr}", f"?page={page_curr+1}"),
                callback=self.parse,
            )
