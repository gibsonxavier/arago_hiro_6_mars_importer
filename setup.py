#!/usr/bin/env python3

import setuptools

name = 'mars_importer'

setuptools.setup(
    version='1.0',
    url="https://github.com/gibsonxavier/mars_importer",
    packages=setuptools.find_packages(),
    install_requires=[
        'graphit-tool',
		'gevent>=1.3.7',
		'docopt>=0.6.2'
		
    ],
    dependency_links=[
        'git+https://github.com/arago/graphit-tool@library#egg=graphit-tool'
    ])
