"""Gitlab's isses objects"""

from .utils import enrich_gitlab_list


def get(gitlab_api):
    """Retrieve current user's issues and adapt the data to be displayed"""
    issues = gitlab_api.issues.list(
        scope="all", state="opened", assignee_id=gitlab_api.user.id
    )
    return enrich_gitlab_list(issues, gitlab_api)
