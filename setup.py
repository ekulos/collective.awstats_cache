# -*- coding: utf-8 -*-
"""Installer for the collective.awstats_cache package."""

from setuptools import find_packages
from setuptools import setup


long_description = '\n\n'.join([
    open('README.rst').read(),
    open('CONTRIBUTORS.rst').read(),
    open('CHANGES.rst').read(),
])


setup(
    name='collective.awstats_cache',
    version='1.0a1',
    description="An add-on for Plone",
    long_description=long_description,
    # Get more from https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
    ],
    keywords='Python Plone',
    author='lucas',
    author_email='luca.pisani@abstract.it',
    url='https://pypi.python.org/pypi/collective.awstats_cache',
    license='GPL version 2',
    packages=find_packages('src', exclude=['ez_setup']),
    namespace_packages=['collective'],
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'plone.api',
        'setuptools',
        'Products.CMFPlone',
        'SQLAlchemy',
        'z3c.saconfig',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
