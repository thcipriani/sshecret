#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
setup sshecret.

Copyright (c) 2017 Tyler Cipriani <tyler@tylercipriani.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the README file
with open(os.path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='sshecret',
    version='20191018',
    description='ssh-agent key management wrapper',
    long_description=long_description,
    url='https://github.com/thcipriani/sshecret',
    author='Tyler Cipriani',
    author_email='tyler@tylercipriani.com',
    license='GNU GPLv3',
    install_requires=[line.strip() for line in open('requirements.txt')],
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
    ],
    keywords='ssh ssh-agent ssh-keygen',
    scripts=['sshecret']
)
