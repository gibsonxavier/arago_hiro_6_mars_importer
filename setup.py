#!/usr/bin/env python3

import setuptools


setuptools.setup(
    name='mars_importer',
    version='1.0.0',
    url="https://github.com/gibsonxavier/mars_importer",
    py_modules=['helper'],
    scripts=['mars_importer'],
    install_requires=[
        'graphit-tool>=0.0',
		'docopt>=0.6.2'
		
    ],
    data_files=[('/usr/local/etc/mars_importer/', ['data/graphit.conf']),('/usr/local/etc/mars_importer/',['data/install.sh'])],
    dependency_links=['https://github.com/arago/graphit-tool@library#egg=graphit-tool-0.7']
    )