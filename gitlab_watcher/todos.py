"""Gitlab's todos objects"""

from .utils import enrich_gitlab_list


def get(gitlab_api):
    """Retrieve current user's todos and adapt the data to be displayed"""
    todos = gitlab_api.todos.list()

    # Required because TODOs are different from Issues and Merge Requests
    for todo in todos:
        todo.project_id = todo.project["id"]
        todo.title = todo.body

    return enrich_gitlab_list(todos, gitlab_api)
