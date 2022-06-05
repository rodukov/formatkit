from setuptools import setup, find_packages
import codecs
import os

VERSION = '1.0.0'
DESCRIPTION = 'Great terminal formatting tool'
LONG_DESCRIPTION = 'A package that can color text, fill text, and format text'

# Setting up
setup(
    name="pythonpackage",
    version=VERSION,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'color', 'formatkit', 'format', 'formatting-tools'],
)