#!/bin/bash

cd "$(dirname "$0")"
. venv/bin/activate
scrapy crawl vinted --loglevel=INFO