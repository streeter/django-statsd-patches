Django Statsd Patches
=====================

These patches are designed to be used with django-statsd-mozilla_.

Installation
------------

From pypi::

        pip install django-statsd-patches

This should install the requirement of django-statsd-mozilla_, but if not,
you can install that with::

        pip install django-statsd-mozilla


Usage
-----

The monkeypatches need to be installed to work. To get them installed,
add the following to your settings.py::

        STATSD_PATCHES = [
                'django_statsd_patches.patches.template',
                'django_statsd_patches.patches.redis_timing',
        ]


Changes
-------

0.0.1:

- First version


.. _django-statsd-mozilla: https://github.com/andymckay/django-statsd
