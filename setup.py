#!/usr/bin/env python

from setuptools import setup, find_packages

classifiers = [
    "Programming Language :: Python",
    "Development Status :: 3 - Alpha",
    "Environment :: Web Environment",
    "Framework :: Django",
]

entry_points = {
    'console_scripts': [
        'sampleapp = SampleApp.manage:main',
    ],
}

setup(
    name='DjangoSampleApp',
    author='Samuele Santi',
    author_email='redshadow@hackzine.org',
    version=__import__('SampleApp').__version__,
    description='Sample django application',
    long_description='Sample django application',
    classifiers=classifiers,
    entry_points=entry_points,
    install_requires=[
        'Django>=1.4,<1.5',  # we want django 1.4
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
