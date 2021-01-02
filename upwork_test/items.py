# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Property(scrapy.Item):
    external_link = scrapy.Field()
    external_id = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    property_type = scrapy.Field()
    square_meters = scrapy.Field()
    room_count = scrapy.Field()
    bathroom_count = scrapy.Field()
    available_date = scrapy.Field()
    images = scrapy.Field()
    city = scrapy.Field()
    zipcode = scrapy.Field()
    address = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    rent = scrapy.Field()
    currency = scrapy.Field()
    deposit = scrapy.Field()
    utilities = scrapy.Field()
    landlord_name = scrapy.Field()
    landlord_email = scrapy.Field()
    landlord_phone = scrapy.Field()
    furnished = scrapy.Field()
    parking = scrapy.Field()
    elevator = scrapy.Field()
    balcony = scrapy.Field()
    terrace = scrapy.Field()
    swimming_pool = scrapy.Field()
    washing_machine = scrapy.Field()
    floor = scrapy.Field()
    dishwasher = scrapy.Field()
    pets_allowed = scrapy.Field()
    energy_label = scrapy.Field()
    prepaid_rent = scrapy.Field()
    floor_plan_images = scrapy.Field()
    water_cost = scrapy.Field()
    heating_cost = scrapy.Field()
    position = scrapy.Field()
