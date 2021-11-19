#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


# Add your dependencies in requirements.txt
# Note: you can add test-specific requirements in tox.ini
requirements = []
with open('requirements.txt') as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)


# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "napari_demo/_version.py"}

setup(
    name='prod-qa-test',
    url='https://github.com/ziyangczi/napari-demo',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    description='laurita plugin demo',
    packages=find_packages(),
    install_requires=requirements,
    use_scm_version=use_scm,
    setup_requires=['setuptools_scm'],
    project_urls={'Source Code': 'https://github.com/chanzuckerberg/napari-demo',
                 'Bug Tracker': 'https://github.com/chanzuckerberg/napari-demo/issues',
                 'Documentation': 'https://github.com/chanzuckerberg/napari-demo',
                 'User Support': 'https://forum.image.sc'},
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Framework :: napari',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    entry_points={
        'napari.plugin': [
            'napari-demo = napari_demo',
        ],
    },
)
