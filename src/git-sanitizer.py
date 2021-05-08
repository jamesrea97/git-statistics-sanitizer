"""This module contains GitSanitizer logic"""
import uuid
import os
from datetime import datetime
import logging
from urllib.parse import urljoin

# import http_request as http_request
import kafka_handler as kafka_handler
from data_handler import sanitize

from dotenv import load_dotenv

load_dotenv('test.env')


class GitStatitisicsUploader:
    def __init__(self):
        self.kafka_endpoint = os.getenv("KAFKA_ENDPOINT")
        self.kafka_consumer_topic = os.getenv("KAFKA_CONSUMER_TOPIC")
        self.kafka_consumer_group = os.getenv("KAFKA_CONSUMER_GROUP")
        self.kafka_producer_topic = os.getenv("KAFKA_PRODUCER_TOPIC")

    async def santize_statistics(self):

        async for message in kafka_handler.consume(self.kafka_endpoint,
                                                   self.kafka_consumer_topic,
                                                   self.kafka_consumer_group):
            import pdb
            pdb.set_trace()

            with open('f', 'w+') as file:
                file.write(message)
            sanitized_data = sanitize(message)

            # TODO publish to event queue when done


async def main():
    g = GitStatitisicsUploader()


    await g.santize_statistics()

if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
    main()
