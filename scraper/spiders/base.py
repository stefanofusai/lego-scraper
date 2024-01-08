import scrapy


class BaseSpider(scrapy.Spider):
    def __init__(self, notify=True, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if notify in {True, "true", "True"}:
            self.notify = True

        elif notify in {False, "false", "False"}:
            self.notify = False

        else:
            raise ValueError("notify must be either true or false")
