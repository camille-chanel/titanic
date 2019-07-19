#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://titanic.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='titanic',
    version='0.1.0',
    description='Playing around with the Titanic dataset.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Camille Crumpton',
    author_email='camille.channell@gmail.com',
    url='https://github.com/camille-chanel/titanic',
    packages=[
        'titanic',
    ],
    package_dir={'titanic': 'titanic'},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='titanic',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
