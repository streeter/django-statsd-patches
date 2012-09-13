from setuptools import setup


setup(
    name='django-statsd-patches',
    version='0.0.2',
    description='Patch and time some additional django libraries',
    long_description=open('README.rst').read(),
    author='Chris Streeter',
    author_email='chris@chrisstreeter.com',
    license='BSD',
    install_requires=['django-statsd-mozilla'],
    packages=['django_statsd_patches',
              'django_statsd_patches/patches'],
    url='https://github.com/streeter/django-statsd-patches',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Framework :: Django'
        ],
    )
