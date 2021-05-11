"""Utilities used by other modules"""

from dataclasses import dataclass
from datetime import datetime

from dateutil.parser import parse
from humanize import naturaltime

projects_cache = {}


def enrich_gitlab_list(elements, gitlab_api):
    """Add `project`, `updated_at_datetime` and `human_relative_time` attribute
    to all the elements"""
    elements = (GitlabElement(element, gitlab_api) for element in elements)
    return sorted(elements, key=lambda i: i.updated_at_datetime, reverse=True)


def get_project_by_id(identifier, gitlab_api):
    """Retrieve the `project` object by its identifier. Use the global
    `projects_cache` variable to limit the number of requets."""
    if identifier not in projects_cache:
        projects_cache[identifier] = gitlab_api.projects.get(identifier)
    return projects_cache[identifier]


@dataclass
class GitlabElement:
    """Class for keeping track of a Gitlab element, handle colors."""

    project: str
    title: str
    labels: str
    updated_at: str
    url: str

    def __init__(self, element, gitlab_api):
        self.title = element.title
        self.project = get_project_by_id(element.project_id, gitlab_api).name
        self.updated_at_datetime = parse(element.updated_at, ignoretz=True)
        self.updated_at = (
            naturaltime(self.updated_at_datetime, when=datetime.utcnow()) or ""
        )

        try:
            self.labels = ", ".join(element.labels)
            self.url = element.web_url
        except AttributeError:
            self.url = element.target_url
            self.labels = ""
