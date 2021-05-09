"""Module contains unit tests for data_handler module"""
import unittest
from uuid import UUID
from datetime import datetime

import context

import data_handler

from test_data import (
    REPO_EXAMPLE
)


class DataHandlerShould(unittest.TestCase):

    def test_sanitize_repo_returns_valid_event(self):
        repos_event = data_handler.sanitize(REPO_EXAMPLE)

        self.assertEqual(repos_event.id_, UUID('d5d24752-3596-4197-a60d-5de17da8716e'))
        self.assertEqual(repos_event.topic, 'repo-sanitized')
        self.assertIsNotNone(repos_event.timestamp)

        repos = repos_event.load

        self.assertEqual(len(repos), 1)

        baro_repo = repos[0]
        self.assertEqual(baro_repo.name, 'baro')
        self.assertEqual(baro_repo.language, 'Kotlin')
        self.assertEqual(baro_repo.default_branch, 'main')
        self.assertEqual(baro_repo.git_url, 'https://github.com/jamesrea97/baro')
        self.assertEqual(baro_repo.created_at, datetime(2021, 3, 14, 14, 8, 14))
        self.assertEqual(baro_repo.updated_at, datetime(2021, 5, 2, 17, 49, 11))


if __name__ == "__main__":

    unittest.main()
