"""Gitlab's merge requests objects"""

from .utils import enrich_gitlab_list


def get(gitlab_api):
    """Retrieve current user's merge requets and adapt the data to be
    displayed"""
    merge_requests = gitlab_api.mergerequests.list(
        scope="all", state="opened", assignee_id=gitlab_api.user.id
    )
    return enrich_gitlab_list(merge_requests, gitlab_api)
