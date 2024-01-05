# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os
import sqlite3
from abc import abstractmethod

import telegram


class BasePipeline:
    TOKEN = os.environ.get("TELEGRAM_TOKEN")
    CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

    def __init__(self):
        self.bot = telegram.Bot(token=self.TOKEN)
        self.db = sqlite3.connect("db.sqlite3")
        cursor = self.db.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS item (
                site TEXT NOT NULL,
                id TEXT NOT NULL,
                data TEXT NOT NULL,
                PRIMARY KEY (site, id)
            );"""
        )
        cursor.close()

    def close_spider(self, spider):
        self.db.commit()
        spider.logger.info(f"Inserted {self.db.total_changes} items")
        self.db.close()

    async def send_telegram_notification(self, spider, item, *, photo):
        if spider.load_db is False:
            await self.bot.send_photo(
                chat_id=self.CHAT_ID,
                photo=photo,
                caption=self.format_message(item),
                parse_mode="Markdown",
                pool_timeout=10,
            )

    @abstractmethod
    def format_message(self, item):
        ...


class SubitoPipeline(BasePipeline):
    async def process_item(self, item, spider):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT 1 FROM item where site = ? AND id = ?", ("subito", item["urn"])
        )
        result = cursor.fetchone()

        if result is None:
            cursor.execute(
                """INSERT INTO item VALUES (
                    :site,
                    :id,
                    :data
                );""",
                {"site": "subito", "id": item["urn"], "data": str(item)},
            )
            cursor.close()

            try:
                photo = item["images"][0]["scale"][-1]["uri"]

            except IndexError:
                photo = None

            await self.send_telegram_notification(spider, item, photo=photo)

        return item

    def format_message(self, item):
        try:
            price = [x for x in item["features"] if x["label"] == "Prezzo"][0][
                "values"
            ][0]["value"]

        except IndexError:
            price = "N/A"

        try:
            shipping_fee = [
                x for x in item["features"] if x["label"] == "Costo della spedizione"
            ][0]["values"][0]["value"]

        except IndexError:
            shipping_fee = None

        message = f"🛍️ [Subito.it - {item['subject']} - {price}]({item['urls']['default']})\n\n"
        message += f"*City:* {item['geo']['city']['value']}\n"

        if shipping_fee is not None:
            message += f"*Shipping fee:* {shipping_fee}\n"

        return message


class VintedPipeline(BasePipeline):
    async def process_item(self, item, spider):
        cursor = self.db.cursor()
        cursor.execute(
            "SELECT 1 FROM item where site = ? AND id = ?", ("vinted", item["id"])
        )
        result = cursor.fetchone()

        if result is None:
            cursor.execute(
                """INSERT INTO item VALUES (
                    :site,
                    :id,
                    :data
                );""",
                {"site": "vinted", "id": item["id"], "data": str(item)},
            )
            cursor.close()
            await self.send_telegram_notification(
                spider, item, photo=item["photo"]["url"]
            )

        return item

    def format_message(self, item):
        # match item["currency"]:
        #     case "EUR":
        #         currency = "€"

        #     case _:
        #         currency = item["currency"]

        if item["currency"] == "EUR":
            currency = "€"

        else:
            currency = item["currency"]

        message = f"🛍️ [Vinted - {item['title']} - {currency} {item['price']}]({item['url']})\n\n"
        message += f"*Brand:* {item['brand_title']}\n"
        message += f"*Favourite Count:* {item['favourite_count']}\n"
        message += (
            f"*Price With Service Fee:* {item['currency']} {item['total_item_price']}\n"
        )
        message += (
            f"*Seller:* [{item['user']['login']}]({item['user']['profile_url']})\n"
        )
        message += f"*Size:* {item['size_title']}\n"
        message += f"*Status:* {item['status']}\n"
        message += f"*View Count:* {item['view_count']}\n\n"
        return message
