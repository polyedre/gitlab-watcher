"""Command line interface for Gitlab Watcher"""

import sys
import argparse

import gitlab
from gitlab_watcher import issues, todos, merge_requests
from gitlab_watcher.display import pretty_print_gitlab_list


def get_parser():
    """Generate the parser for the command line"""
    parser = argparse.ArgumentParser(
        description="GitLab Watcher Command Line Interface"
    )
    parser.add_argument("--config", help="Config file")
    parser.add_argument("--url", required=True, help="Url of the Gitlab instance")
    parser.add_argument(
        "--access-token", required=True, help="Access token to interact with Gitlab"
    )
    return parser


def main():
    """Main command line function"""
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])

    gitlab_api = gitlab.Gitlab(args.url, private_token=args.access_token)
    gitlab_api.auth()

    pretty_print_gitlab_list(issues.get(gitlab_api), "ISSUES")
    pretty_print_gitlab_list(merge_requests.get(gitlab_api), "MERGE REQUESTS")
    pretty_print_gitlab_list(todos.get(gitlab_api), "TODOs")
