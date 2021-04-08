"""Generic print function for Gitlab's elements"""

from colorama import Fore, Style


def pretty_print_gitlab_list(elements, name):
    """Print a section named `name` containing all the `elements`.
    For each element, its title, the relative date it was last updated at and
    the related project name are printed."""
    print_section_title(f"{name} ({len(elements)})")
    for element in elements:
        print(
            f"{element.project.name:20.20s}",
            f"{Fore.YELLOW if element.title.startswith('Draft: ') else Fore.GREEN}",
            f"{Style.BRIGHT}{element.title:100.100s}{Style.RESET_ALL}",
            f"{Style.DIM}{element.human_relative_time}{Style.RESET_ALL}",
        )


def print_section_title(name):
    """Print the title of a new section"""
    print(f"{Style.BRIGHT}{Fore.MAGENTA}{name}{Style.RESET_ALL}")


def section_separator():
    """Print the separator between 2 sections"""
    print()
