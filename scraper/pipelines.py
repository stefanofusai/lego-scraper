# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os
import sqlite3

import telegram

from scraper.utils import format_price


class ScraperPipeline:
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
                url TEXT NOT NULL,
                image TEXT,
                title TEXT NOT NULL,
                currency TEXT NOT NULL,
                price REAL NOT NULL,
                condition TEXT,
                in_stock BOOLEAN,
                PRIMARY KEY (site, id)
            );"""
        )
        cursor.close()

    def close_spider(self, spider):
        self.db.commit()
        spider.logger.info(f"Inserted {self.db.total_changes} items")
        self.db.close()

    async def process_item(self, item, spider):
        cursor = self.db.cursor()
        cursor.execute(
            """SELECT
                site,
                id,
                url,
                image,
                title,
                currency,
                price,
                condition,
                in_stock
            FROM
                item
            WHERE
                site = ?
                AND id = ?;""",
            (item["site"], item["id"]),
        )
        row = cursor.fetchone()
        site, id, url, image, title, currency, price, condition, _in_stock = row
        in_stock = bool(_in_stock)

        if row is None:
            cursor.execute(
                """INSERT INTO item VALUES (
                    :site,
                    :id,
                    :url,
                    :image,
                    :title,
                    :currency,
                    :price,
                    :condition,
                    :in_stock
                );""",
                {
                    "site": item["site"],
                    "id": item["id"],
                    "url": item["url"],
                    "image": item["image"],
                    "title": item["title"],
                    "currency": item["currency"],
                    "price": item["price"],
                    "condition": item["condition"],
                    "in_stock": item["in_stock"],
                },
            )

            if spider.load_db is False:
                await self.send_telegram_notification(item, reason="New item")

        elif item["price"] != price:
            cursor.execute(
                "UPDATE item SET price = ?, in_stock = ? WHERE site = ? AND id = ?;",
                (item["price"], item["in_stock"], item["site"], item["id"]),
            )

            if spider.load_db is False and item["price"] <= price * 0.95:
                if item["in_stock"] is True and in_stock is False:
                    reason = f"Item restocked and price dropped from {currency}{format_price(price)} to {item['currency']}{format_price(item['price'])} by {format_price(round(((item['price'] - price) / price) * 100, 2))}%"

                elif item["in_stock"] is False and in_stock is True:
                    reason = f"Item sold out and price dropped from {currency}{format_price(price)} to {item['currency']}{format_price(item['price'])} by {format_price(round(((item['price'] - price) / price) * 100, 2))}%"

                else:
                    reason = f"Price dropped from {currency}{format_price(price)} to {item['currency']}{format_price(item['price'])} by {format_price(round(((item['price'] - price) / price) * 100, 2))}%"

                await self.send_telegram_notification(item, reason=reason)

        elif item["in_stock"] != in_stock:
            cursor.execute(
                "UPDATE item SET in_stock = ? WHERE site = ? AND id = ?;",
                (item["in_stock"], item["site"], item["id"]),
            )

            if spider.load_db is False and item["in_stock"] is True:
                await self.send_telegram_notification(item, reason="Item restocked")

        cursor.close()
        return item

    async def send_telegram_notification(self, item, *, reason):
        caption = f"{reason}: [{item['title']}]({item['url']})\n"
        caption += "```\n"
        caption += f"Site: {item['site']}\n"
        caption += f"Price: {item['currency']}{format_price(item['price'])}\n"

        if item["condition"] is not None:
            caption += f"Condition: {item['condition']}\n"

        caption += "```"

        try:
            await self.bot.send_photo(
                chat_id=self.CHAT_ID,
                photo=item["image"],
                caption=caption,
                parse_mode="Markdown",
                pool_timeout=10,
            )

        except telegram.error.BadRequest:
            await self.bot.send_message(
                chat_id=self.CHAT_ID,
                text=caption,
                parse_mode="Markdown",
                pool_timeout=10,
            )
