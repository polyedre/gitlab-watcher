"""Generic print function for Gitlab's elements"""

from colorama import Fore, Style


def pretty_print_gitlab_list(elements, name):
    """Print a section named `name` containing all the `elements`.
    For each element, its title, the relative date it was last updated at and
    the related project name are printed."""
    print_section_title(f"{name} ({len(elements)})")
    for element in elements:
        element.title_and_labels = (
            f"{Style.BRIGHT}{Fore.YELLOW if element.title.startswith('Draft: ') else Fore.GREEN}{element.title}   "
            f"{Style.DIM}{Fore.RED}{', '.join(element.labels)}{Style.RESET_ALL}"
        )
        print(
            f"{element.project.name:20.20s}",
            f"{element.title_and_labels:120.120s}",
            f"{Style.DIM}{element.human_relative_time:12.12s}{Style.RESET_ALL}",
            f"{Fore.BLUE}{Style.DIM}{element.web_url}{Style.RESET_ALL}",
        )


def print_section_title(name):
    """Print the title of a new section"""
    print(f"{Style.BRIGHT}{Fore.MAGENTA}{name}{Style.RESET_ALL}")


def section_separator():
    """Print the separator between 2 sections"""
    print()
