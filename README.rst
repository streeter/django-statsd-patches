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
add the following to your `settings.py`::

    STATSD_PATCHES = [
        'django_statsd_patches.patches.template',
        'django_statsd_patches.patches.redis_timing',
    ]

By default both the `template` and `redis_timing` patches sample every
call. To add sampling to the calls, define one or both of the following
settings in your `settings.py`::


    STATSD_REDIS_SAMPLE_RATE = 0.5
    STATSD_TEMPLATE_SAMPLE_RATE = 0.25

Then you'll get sampling of the calls.


Changes
-------

0.0.2:

- Added `STATSD_REDIS_SAMPLE_RATE` and `STATSD_TEMPLATE_SAMPLE_RATE`
- Changed redis statsd keys

0.0.1:

- First version


.. _django-statsd-mozilla: https://github.com/andymckay/django-statsd
