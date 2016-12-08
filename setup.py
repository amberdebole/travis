""" Setup Django-Markdown. """

import os

from setuptools import setup, find_packages
import re


MODULE_NAME = 'travis_test'
PACKAGE_DATA = list()

download_url = "https://github.com/sv0/travis/archive/0.0.1.tar.gz"

setup(
    name='travis_test',
    version='0.0.1',
    description='',
    long_description='',
    license='',

    author="Kirill Klenov",
    author_email="horneds@gmail.com",
    maintainer="Slavik Svyrydiuk",
    maintainer_email="svyrydiuk@gmail.com",
    url="https://github.com/sv0/django-markdown-app",
    download_url=download_url,

    keywords='html markdown django',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Framework :: Django :: 1.10',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',  # noqa
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Text Processing :: Markup',
    ],

    packages=find_packages(),
    package_data={'': PACKAGE_DATA, },

    #install_requires=install_requires,
)

# pylama:ignore=C0111
