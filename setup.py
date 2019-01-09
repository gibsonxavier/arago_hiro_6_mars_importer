#!/usr/bin/env python3

import setuptools


setuptools.setup(
    name='mars_importer',
    version='1.0',
    url="https://github.com/gibsonxavier/mars_importer",
    scripts=['put_mars_nodes.py'],
    py_modules=['helper'],
    install_requires=[
        'graphit-tool',
		'docopt>=0.6.2'
		
    ],
    data_files=[('/usr/local/etc/mars_importer/', ['data/graphit.conf']),('/usr/local/etc/mars_importer/',['data/install.sh'])],
    dependency_links=['git+https://github.com/arago/graphit-tool@library#egg=graphit-tool']
    )