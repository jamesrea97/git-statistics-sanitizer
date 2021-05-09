"""This module contains the event of this service"""

from dataclasses import dataclass
from datetime import datetime
from typing import Union
import uuid

from git_objects import Repo
@dataclass
class Event:
    id_: uuid
    topic: str
    timestamp: datetime
    load: list[Union[Repo]]

    def to_json(self):
        return {
            "id_": str(self.id_),
            "topic": self.topic,
            "timestamp": str(self.timestamp),
            "load": [e.to_json() for e in self.load]
        }
