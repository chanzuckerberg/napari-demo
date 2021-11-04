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
    name='staging plugin test creation',
    author='Laura Marcos',
    author_email='lmarcos@chanzuckerberg.com',
    license='MIT',
    url='https://github.com/ziyangczi/napari-demo',
    summary= 'Pipelines and pipeline components for the analysis of image-based transcriptomics data',
    description='Build scalable pipelines that localize and quantify RNA transcripts in image data generated by any FISH method',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6','>=3.7','>=3.8',
    install_requires=requirements,
    use_scm_version=use_scm,
    setup_requires=['setuptools_scm'],
    project_urls={'Source Code': 'https://github.com/ziyangczi/napari-demo'},
         'Bug Tracker = https://github.com/spacetx/starfish/issues',
         'Documentation = https://spacetx-starfish.readthedocs.io/en/latest/',
         'Source Code = https://github.com/spacetx/starfish',
         'User Support = https://forum.image.sc/tag/starfish',
         'Twitter = https://twitter.com/napari_imaging',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Framework :: napari',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',  
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: BSD License',
    ],
    entry_points={
        'napari.plugin': [
            'napari-demo = napari_demo',
        ],
    },
)
