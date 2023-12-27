import scrapy

from scraper.items import VintedItem


class VintedSpider(scrapy.Spider):
    name = "vinted"

    def start_requests(self):
        yield scrapy.Request(
            "https://www.vinted.it/catalog?search_text=lego&status_ids[]=6&status_ids[]=1",
            callback=self._start_requests,
        )

    def _start_requests(self, response):
        yield scrapy.Request(
            "https://www.vinted.it/api/v2/catalog/items?page=1&per_page=984&search_text=lego&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=6,1&order=newest_first",
            callback=self.parse,
        )

    def parse(self, response):
        for item in response.json()["items"]:
            yield VintedItem(
                id=item["id"],
                title=item["title"],
                price=item["price"],
                is_visible=item["is_visible"],
                discount=item["discount"],
                currency=item["currency"],
                brand_title=item["brand_title"],
                is_for_swap=item["is_for_swap"],
                user=item["user"],
                url=item["url"],
                promoted=item["promoted"],
                photo=item["photo"],
                favourite_count=item["favourite_count"],
                is_favourite=item["is_favourite"],
                badge=item["badge"],
                conversion=item["conversion"],
                service_fee=item["service_fee"],
                total_item_price=item["total_item_price"],
                total_item_price_rounded=item["total_item_price_rounded"],
                view_count=item["view_count"],
                size_title=item["size_title"],
                content_source=item["content_source"],
                status=item["status"],
                icon_badges=item["icon_badges"],
                search_tracking_params=item["search_tracking_params"],
            )

        page_curr = response.json()["pagination"]["current_page"]

        if page_curr < response.json()["pagination"]["total_pages"]:
            yield scrapy.Request(
                f"https://www.vinted.it/api/v2/catalog/items?page={page_curr+1}&per_page=984&search_text=lego&catalog_ids=&color_ids=&brand_ids=&size_ids=&material_ids=&video_game_rating_ids=&status_ids=6,1&order=newest_first",
                callback=self.parse,
            )
