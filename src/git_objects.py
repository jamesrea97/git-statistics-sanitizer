"""This module contains the git_objects of this service"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Repo:
    name: str
    created_at: datetime
    updated_at: datetime
    default_branch: str
    language: str
    git_url: str

    def to_json(self):
        return {
            'name': self.name,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'default_branch': self.default_branch,
            'language': self.language,
            'git_url': self.git_url,
        }
