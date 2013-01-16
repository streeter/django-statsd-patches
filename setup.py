#!/usr/bin/env python

version = '0.0.3'

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


packages = [
    'django_statsd_patches',
    'django_statsd_patches/patches'
]

requires = [
    'django-statsd-mozilla',
]

setup(
    name='django-statsd-patches',
    version=version,
    description='Patch and time some additional django libraries',
    long_description=open('README.rst').read(),
    author='Chris Streeter',
    author_email='chris@chrisstreeter.com',
    license=open('LICENSE').read(),
    install_requires=requires,
    packages=packages,
    url='https://github.com/streeter/django-statsd-patches',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    )
