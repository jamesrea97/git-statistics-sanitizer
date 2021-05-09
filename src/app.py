"""This module contains the main driver of the service"""
import os
import asyncio
import logging
from dotenv import load_dotenv

from git_sanitizer import GitStatisticsSanitizer

load_dotenv('.env')


def setup_logging():
    log_level = os.getenv('LOGGING_LEVEL', logging.INFO)
    logging.basicConfig(
        filename='service.log',
        filemode='a',
        level=log_level,
        format='%(asctime)s git-sanitizer %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p')


def main():
    setup_logging()
    # TODO add rest_interface logic
    sanitizer = GitStatisticsSanitizer()
    asyncio.run(sanitizer.santize_statistics())


if __name__ == "__main__":
    main()
