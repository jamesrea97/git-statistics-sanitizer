"""This module contains data handling logic"""
import os
from datetime import datetime
import uuid
from git_objects import (
    Repo
)
from event import Event


def sanitize(load: str):
    topic = load['topic']

    # TODO Add commit topics, etc as needed
    if topic == os.getenv('KAFKA_REPO_UPLOADED_TOPIC'):
        return _sanitize_repos(load)


def _sanitize_repos(repos_load: dict[str, str]) -> Event:
    request_id = repos_load['id_']
    load = repos_load['load']

    repos = []
    for json_repo in load:
        name = json_repo['name']
        created_at = json_repo['created_at']
        updated_at = json_repo['updated_at']
        default_branch = json_repo['default_branch']
        language = json_repo['language']
        git_url = json_repo['svn_url']

        repo = Repo(name=name,
                    created_at=datetime.strptime(created_at, '%Y-%m-%dT%H:%M:%SZ'),
                    updated_at=datetime.strptime(updated_at, '%Y-%m-%dT%H:%M:%SZ'),
                    default_branch=default_branch,
                    language=language,
                    git_url=git_url)
        repos.append(repo)

    return Event(
        id_=uuid.UUID(request_id),
        topic=os.getenv('KAFKA_REPO_SANITIZED'),
        timestamp=datetime.utcnow(),
        load=repos
    )
