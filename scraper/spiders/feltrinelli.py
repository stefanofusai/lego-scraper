import scrapy

from scraper.items import Item
from scraper.spiders.base import BaseSpider


class FeltrinelliSpider(BaseSpider):
    name = "feltrinelli"

    allowed_domains = ["q6tq74ht1y-dsn.algolia.net"]
    start_urls = [
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=40539&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=40615&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=40623&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=40624&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=40625&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=40626&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75290&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75300&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75301&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75304&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75312&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75320&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75323&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75324&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75327&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75329&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75330&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75333&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75336&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75342&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75345&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75347&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75348&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75350&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75351&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75352&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75353&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75354&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75356&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75359&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75360&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75361&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75364&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
        "https://q6tq74ht1y-dsn.algolia.net/1/indexes/prod_NewFCOM?query=75369&filters=publisher:LEGO&x-algolia-agent=Algolia%20for%20JavaScript%20(4.8.3)%3B%20Browser%20(lite)%3B%20instantsearch.js%20(4.8.3)%3B%20Vue%20(2.6.12)%3B%20Vue%20InstantSearch%20(3.4.2)%3B%20JS%20Helper%20(3.2.2)&x-algolia-api-key=7b36cc1e107cf27466c52564a1177f0d&x-algolia-application-id=Q6TQ74HT1Y",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse, cb_kwargs={"url": url})

    def parse(self, response, url):
        for result in response.json()["hits"]:
            if url.split("query=")[1].split("&")[0] in result["title"]:
                break

        else:
            return

        yield Item(
            site="Feltrinelli",
            id=result["objectID"],
            url=f"https://www.lafeltrinelli.it{result['productUrl']}",
            image=result["image"],
            title=result["title"],
            currency="€",
            price=result["price"],
            condition=None,
            in_stock=True,
        )
