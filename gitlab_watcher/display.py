"""Generic print function for Gitlab's elements"""

from gitlab_watcher.utils import GitlabElement
from rich.console import Console
from rich.table import Table
from rich import box


def pretty_print_gitlab_list(elements: list[GitlabElement], name):
    """Print a section named `name` containing all the `elements`.
    For each element, its title, the relative date it was last updated at and
    the related project name are printed."""
    if not elements:
        return

    table = Table(title=name, box=box.ROUNDED)

    table.add_column("Project", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Labels", justify="center", style="green")
    table.add_column("Updated at", justify="left", style="green")
    table.add_column("URL", justify="left", style="blue")

    for element in elements:
        table.add_row(
            element.project,
            element.title,
            element.labels,
            element.updated_at,
            element.url,
            style="dim" if element.title.startswith("Draft:") else "bold",
        )

    Console().print(table)
