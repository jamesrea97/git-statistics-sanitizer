"""This module contains GitSanitizer logic"""
import os
import logging
from sanic import Sanic

import kafka_handler as kafka_handler
from data_sanitizer import sanitize


class GitStatisticsSanitizer:
    def __init__(self, app: Sanic = None):
        self.app = app
        self.kafka_endpoint = os.getenv("KAFKA_ENDPOINT")
        self.kafka_consumer_repo_topic = os.getenv("KAFKA_REPO_UPLOADED_TOPIC")
        self.kafka_consumer_repo_consumer_group = os.getenv("KAFKA_REPO_UPLOADED_CONSUMER_GROUP")
        self.kafka_producer_repo_topic = os.getenv("KAFKA_REPO_SANITIZED")

    async def santize_statistics(self):

        async for message in kafka_handler.consume(self.kafka_endpoint,
                                                   self.kafka_consumer_repo_topic,
                                                   self.kafka_consumer_repo_consumer_group):

            logging.info(f'Message {message["id_"]} received - Topic: {message["topic"]}.')

            event = sanitize(message)

            await kafka_handler.publish(self.kafka_endpoint,
                                        event.topic,
                                        event.to_json())

            logging.info(f'Message {str(event.id_)} published - Topic: {event.topic}.')
