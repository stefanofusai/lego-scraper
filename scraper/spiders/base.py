import scrapy


class BaseSpider(scrapy.Spider):
    def __init__(self, load_db=False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if load_db in {True, "true", "True"}:
            self.load_db = True

        elif load_db in {False, "false", "False"}:
            self.load_db = False

        else:
            raise ValueError("load_db must be either true or false")
