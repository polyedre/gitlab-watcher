"""Generic print function for Gitlab's elements"""

from dataclasses import asdict, dataclass
from colorama import Fore, Style
from gitlab_watcher.utils import GitlabElement


def pretty_print_gitlab_list(elements, name):
    """Print a section named `name` containing all the `elements`.
    For each element, its title, the relative date it was last updated at and
    the related project name are printed."""
    if not elements:
        return

    fields_length = get_column_width(GitlabElement, elements)

    colorised_elements = (
        GitlabColoredElement(
            **{key: ColorisedString(value) for key, value in asdict(element).items()}
        )
        for element in elements
    )

    print_section_title(f"{name} ({len(elements)})")
    for element in colorised_elements:
        print(
            " ".join(
                getattr(element, field).to_string(length) if length else ""
                for field, length in fields_length.items()
            )
        )


def get_column_width(dataclass_class, elements):
    """Return a dictionnary that associate each field with the lenght of the
    biggest field"""
    return {
        field: max((len(element.__getattribute__(field)) for element in elements))
        for field in dataclass_class.__dataclass_fields__
    }


def print_section_title(name):
    """Print the title of a new section"""
    print(f"{Style.BRIGHT}{Fore.MAGENTA}{name}{Style.RESET_ALL}")


def section_separator():
    """Print the separator between 2 sections"""
    print()


class ColorisedString:
    """Class to add colors and keep the right length"""

    def __init__(self, content, style="", color=""):
        self.content = content
        self.style = style
        self.color = color

    def __len__(self):
        """Return the content length"""
        return len(self.content)

    def to_string(self, length=None):
        """Return a string with color codes included"""
        if length:
            fstring = (
                f"{self.style}{self.color}{{:{length}.{length}s}}{Style.RESET_ALL}"
            )
        else:
            fstring = f"{self.style}{self.color}{{}}{Style.RESET_ALL}"
        return fstring.format(self.content)


@dataclass
class GitlabColoredElement:
    """Class for keeping track of a Gitlab element, handle colors."""

    project: ColorisedString
    title: ColorisedString
    labels: ColorisedString
    updated_at: ColorisedString
    url: ColorisedString

    def __post_init__(self):
        self.title.style = Style.BRIGHT
        self.title.color = (
            Fore.YELLOW if self.title.content.startswith("Draft: ") else Fore.GREEN
        )
        self.labels.style = Style.DIM
        self.labels.color = Fore.RED
        self.updated_at.style = Style.DIM
        self.url.style = Style.DIM
        self.url.color = Fore.BLUE
