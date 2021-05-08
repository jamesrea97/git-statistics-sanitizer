"""This module contains data handling logic"""
import json

from datetime import datetime
import uuid
from git_objects import (
    Repo
)
from event import Event


def sanitize(load):
    # TODO add more as there are more functionalities
    topic = load['topic']

    if topic == 'git-uploaded':
        return _sanitize_repos(load)


def _sanitize_repos(repos_load: dict[str, str]) -> Event:
    request_id = repos_load['id_']
    load = repos_load['load']
    json_repos = json.loads(load)

    repos = []
    for json_repo in json_repos:
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
        topic='git-sanitized',  # TODO change this if required
        timestamp=datetime.utcnow(),
        load=repos
    )
