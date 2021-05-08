"""This module contains data handling logic"""
import json
from typing import Any
from datetime import datetime
import uuid
from data_objects import (
    Repo
)
from event_objects import Event


def sanitize_repos(repos_load: dict[str, str]) -> dict[str, Any]:
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
