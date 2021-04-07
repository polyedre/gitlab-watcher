"""Utilities used by other modules"""

from dateutil.parser import parse
from humanize import naturaltime

projects_cache = {}


def enrich_gitlab_list(elements, gitlab_api):
    """Add `project`, `updated_at_datetime` and `human_relative_time` attribute
    to all the elements"""
    for element in elements:
        element.project = get_project_by_id(element.project_id, gitlab_api)
        element.updated_at_datetime = parse(element.updated_at, ignoretz=True)
        element.human_relative_time = naturaltime(element.updated_at_datetime)

    return sorted(elements, key=lambda i: i.updated_at_datetime, reverse=True)


def get_project_by_id(identifier, gitlab_api):
    """Retrieve the `project` object by its identifier. Use the global
    `projects_cache` variable to limit the number of requets."""
    if identifier not in projects_cache:
        projects_cache[identifier] = gitlab_api.projects.get(identifier)
    return projects_cache[identifier]
