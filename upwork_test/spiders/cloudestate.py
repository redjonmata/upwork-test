#!/usr/bin/env python
# -*- coding: utf-8 -*-

import scrapy
from upwork_test.items import Property
from scrapy.loader import ItemLoader
import re


class DiedeutscheSpider(scrapy.Spider):
    name = 'cloudestate'
    start_urls = ['https://www.cloud9estates.co.uk/properties/lettings']

    def parse(self, response):
        for property in response.css('.property-listing .info'):
            url = property.css('a:nth-child(2)::attr(href)').get()

            yield scrapy.Request('https://www.cloud9estates.co.uk' + url, self.parse_property)

        for next_page in response.css('.next'):
            yield response.follow(next_page, self.parse)

    def parse_property(self, response):
        estate_property = ItemLoader(item=Property(), response=response)

        title = response.css('#property-show h3').xpath('normalize-space()').get()
        description = response.xpath('//*[@id="description"]').xpath('normalize-space()').get()
        split_title = title.split(',')
        title_length = len(split_title)
        property_type = response.css('.property_type').xpath('normalize-space()').get()
        room_count = response.css('.bedrooms .no').xpath('normalize-space()').get()
        bathroom_count = response.css('.bathrooms .no').xpath('normalize-space()').get()
        rent = response.css('.price').xpath('normalize-space()').get()
        rent_no = int(re.search(r'\d+', rent).group())

        if '$' in rent:
            currency = 'USD'
        elif '€' in rent:
            currency = 'EUR'
        elif '£' in rent:
            currency = 'GBP'
        else:
            currency = 'NONE'

        estate_property.add_value('external_link', response.url)
        estate_property.add_value('title', title)
        estate_property.add_value('description', description)
        estate_property.add_value('address', title)
        estate_property.add_value('city', split_title[title_length - 2])
        estate_property.add_value('zipcode', split_title[title_length - 1])
        estate_property.add_value('property_type', property_type)
        estate_property.add_value('room_count', room_count)
        estate_property.add_value('bathroom_count', bathroom_count)
        estate_property.add_value('rent', rent_no)
        estate_property.add_value('currency', currency)

        yield estate_property.load_item()