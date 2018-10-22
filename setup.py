#!/usr/bin/env python
 
from setuptools import setup, find_packages
 
setup(
    name="sample-n-files",
    version="1.0",
    author="Marco Pantaleoni",
    description="Randomly sample N files from a directory.",
    py_modules=['sample_n_files'],
    install_requires=[
    	'Click'
    ],
    entry_points='''
        [console_scripts]
        sample-n-files=sample_n_files:cli
    ''',
    packages=find_packages()
)