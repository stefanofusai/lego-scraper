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
        self.db = sqlite3.connect("vinted.db")

        cursor = self.db.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS item (
                id INTEGER NOT NULL PRIMARY KEY,
                title TEXT NOT NULL,
                price REAL NOT NULL,
                is_visible INTEGER NOT NULL,
                discount TEXT,
                currency TEXT NOT NULL,
                brand_title TEXT NOT NULL,
                user TEXT NOT NULL,
                url TEXT NOT NULL,
                promoted INTEGER NOT NULL,
                photo TEXT NOT NULL,
                favourite_count INTEGER NOT NULL,
                is_favourite INTEGER NOT NULL,
                badge TEXT,
                conversion TEXT,
                service_fee REAL NOT NULL,
                total_item_price REAL NOT NULL,
                total_item_price_rounded REAL,
                view_count INTEGER NOT NULL,
                size_title TEXT NOT NULL,
                content_source TEXT NOT NULL,
                status TEXT NOT NULL,
                icon_badges TEXT NOT NULL,
                search_tracking_params TEXT NOT NULL
            );"""
        )
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_item_id ON item (id);")
        cursor.close()

    async def process_item(self, item, spider):
        cursor = self.db.cursor()
        cursor.execute("SELECT id FROM item WHERE id = ?", (item["id"],))
        result = cursor.fetchone()

        if result is None:
            cursor.execute(
                """INSERT INTO item VALUES (
                    :id,
                    :title,
                    :price,
                    :is_visible,
                    :discount,
                    :currency,
                    :brand_title,
                    :user,
                    :url,
                    :promoted,
                    :photo,
                    :favourite_count,
                    :is_favourite,
                    :badge,
                    :conversion,
                    :service_fee,
                    :total_item_price,
                    :total_item_price_rounded,
                    :view_count,
                    :size_title,
                    :content_source,
                    :status,
                    :icon_badges,
                    :search_tracking_params
                );""",
                {
                    "id": item["id"],
                    "title": item["title"],
                    "price": item["price"],
                    "is_visible": item["is_visible"],
                    "discount": item["discount"],
                    "currency": item["currency"],
                    "brand_title": item["brand_title"],
                    "user": str(item["user"]),
                    "url": item["url"],
                    "promoted": item["promoted"],
                    "photo": str(item["photo"]),
                    "favourite_count": item["favourite_count"],
                    "is_favourite": item["is_favourite"],
                    "badge": item["badge"],
                    "conversion": item["conversion"],
                    "service_fee": item["service_fee"],
                    "total_item_price": item["total_item_price"],
                    "total_item_price_rounded": item["total_item_price_rounded"],
                    "view_count": item["view_count"],
                    "size_title": item["size_title"],
                    "content_source": item["content_source"],
                    "status": item["status"],
                    "icon_badges": str(item["icon_badges"]),
                    "search_tracking_params": str(item["search_tracking_params"]),
                },
            )

            if getattr(spider, "load_db", "false") != "true":
                await self.bot.send_photo(
                    chat_id=self.CHAT_ID,
                    photo=item["photo"]["url"],
                    caption=self.format_message(item),
                    parse_mode="Markdown",
                    pool_timeout=10,
                )

        cursor.close()
        return item

    def close_spider(self, spider):
        self.db.commit()
        spider.logger.info(f"Inserted {self.db.total_changes} items")
        self.db.close()

    def format_message(self, item):
        message = f"🛍️ [New Item For Sale!]({item['url']})\n\n"
        message += f"*Brand:* {item['brand_title']}\n"
        message += f"*Favourite Count:* {item['favourite_count']}\n"
        message += f"*Price:* {item['currency']} {item['price']}\n"
        message += (
            f"*Price With Service Fee:* {item['currency']} {item['total_item_price']}\n"
        )
        message += (
            f"*Seller:* [{item['user']['login']}]({item['user']['profile_url']})\n"
        )
        message += f"*Size:* {item['size_title']}\n"
        message += f"*Status:* {item['status']}\n"
        message += f"*Title:* {item['title']}\n"
        message += f"*View Count:* {item['view_count']}\n\n"
        return message
