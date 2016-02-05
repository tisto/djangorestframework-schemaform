# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='djangorestframework-schemaform',
    use_scm_version=True,
    license='BSD',
    author='Timo Stollenwerk',
    author_email='tisto@plone.org',
    description='Angular Schema Form add-on for Django Rest Framework',
    url='https://github.com/tisto/djangorestframework-schemaform',
    keywords=['django', 'rest-framework', 'json', 'schemaform', 'angular'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=['django', 'djangorestframework'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ]
)
