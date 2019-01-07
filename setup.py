import setuptools



setuptools.setup(
    name="put_mars_nodes",
    version="0.0.1",
    author="Gibson Xavier",
    author_email="gxavier@arago.co",
    description="Tool to import MARS model data",
    long_description="Tool to import MARS model data created by the Java Excel to MARS utility for HIRO 6",
    url="https://github.com/gibsonxavier/mars_importer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'graphit-tool>=0.7',
		'gevent>=1.3.7',
		'docopt>=0.6.2',
		'helper>=0.0.0',
		
    ],
    dependency_links=[
        'git+https://github.com/arago/graphit-tool@library',
		'git+https://github.com/gibsonxavier/mars_importer/blob/master/helper.py'
    ]
