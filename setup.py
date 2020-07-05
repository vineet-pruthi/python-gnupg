#!/usr/bin/env python

import sys
from os.path import abspath, dirname, join


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


VERSION = None
version_file = join(dirname(abspath(__file__)), 'gnupg', 'version.py')
with open(version_file) as file:
    code = compile(file.read(), version_file, 'exec')
    exec(code)


DESCRIPTION = """
This module allows easy access to GnuPG's key
management, encryption and signature functionality from Python programs.
It is intended for use with Python 2.4 or greater.
"""[1:-1]


CLASSIFIERS = """
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Operating System :: OS Independent
Topic :: Software Development :: Libraries :: Python Modules
"""[1:-1]


setup(name = "python-gnupg",
    description="A wrapper for the Gnu Privacy Guard (GPG or GnuPG)",
    long_description=DESCRIPTION,
    license="""Copyright (C) 2008-2019 by Vinay Sajip. All Rights Reserved. See LICENSE.txt for license.""",
    version=VERSION,
    author="Vinay Sajip",
    author_email="vinay_sajip@red-dove.com",
    maintainer="Vinay Sajip",
    maintainer_email="vinay_sajip@red-dove.com",
    url="https://docs.red-dove.com/python-gnupg/",
    py_modules=["gnupg"],
    platforms="No particular restrictions",
    download_url="https://pypi.io/packages/source/p/python-gnupg/python-gnupg-%s.tar.gz" % VERSION,
    classifiers=CLASSIFIERS.splitlines(),
    keywords='python-gnupg gnupg gpg',
    packages=['gnupg']
)
