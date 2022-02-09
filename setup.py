#!/usr/bin/env python
__usage__ = "setup.py command [--options]"
__description__ = "standard install script"
__author__ = "katherine.karababas@mail.utoronto.ca"

#-------------------------------------------------

from setuptools import (setup, find_packages)
import glob

setup(
    name = 'sodapop',
    version = '0.0',
    url = 'https://github.com/katherinekarababas/sodapop-em',
    author = __author__,
    author_email = 'katherine.karababas@mail.utoronto.ca',
    description = __description__,
    license = '',
    scripts = glob.glob('bin/*'),
    packages = find_packages(),
    data_files = [],
    requires = [],
)
