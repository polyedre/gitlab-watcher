#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
from setuptools import find_packages

setup(
    name="gitlab-watcher",
    version="0.1",
    description="Gitlab activity watcher utility",
    author="polyedre",
    author_email="polyedre@disroot.org",
    packages=find_packages(),
    entry_points={"console_scripts": ["gitlab-watcher = gitlab_watcher.cli:main"]},
)
