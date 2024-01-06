# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import os
import sqlite3

import telegram


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
                CONDITION
            FROM
                item
            WHERE
                site = ?
                AND id = ?;""",
            (item["site"], item["id"]),
        )
        result = cursor.fetchone()

        if result is None:
            cursor.execute(
                """INSERT INTO item VALUES (
                    :site,
                    :id,
                    :url,
                    :image,
                    :title,
                    :currency,
                    :price,
                    :condition
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
                },
            )

            if spider.load_db is False:
                await self.send_telegram_notification(item, reason="New item")

        elif result[6] != item["price"]:
            cursor.execute(
                "UPDATE item SET price = ? WHERE site = ? AND id = ?",
                (item["price"], item["site"], item["id"]),
            )

            if spider.load_db is False:
                await self.send_telegram_notification(
                    item,
                    reason=f"Price changed from {result[5]}{result[6]} to {item['currency']}{item['price']}",
                )

        cursor.close()

        return item

    async def send_telegram_notification(self, item, *, reason):
        caption = f"{reason}: [{item['title']}]({item['url']})\n"
        caption += "```\n"
        caption += f"Site: {item['site']}\n"

        if int(item["price"]) == item["price"]:
            price = int(item["price"])

        else:
            price = item["price"]

        caption += f"Price: {item['currency']}{price}\n"

        if item["condition"] is not None:
            caption += f"Condition: {item['condition']}\n"

        caption += "```"

        await self.bot.send_photo(
            chat_id=self.CHAT_ID,
            photo=item["image"],
            caption=caption,
            parse_mode="Markdown",
            pool_timeout=10,
        )
