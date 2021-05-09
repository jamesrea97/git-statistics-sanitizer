"""This module contains the main driver of the service"""
import asyncio
from dotenv import load_dotenv

from git_sanitizer import GitStatisticsSanitizer

load_dotenv('.env')

def main():
    # TODO add rest_interface logic
    sanitizer = GitStatisticsSanitizer()
    asyncio.run(sanitizer.santize_statistics())


if __name__ == "__main__":
    main()
