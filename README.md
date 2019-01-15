# arago_hiro_6_mars_importer
Python script to import MARS model for HIRO version 6.x

Requires Python 3.

Install the GraphIT Lib tools first
```bash
pip install git+https://github.com/arago/graphit-tool@library
```
Install the mars_importer

```bash
pip install git+https://github.com/gibsonxavier/mars_importer
```
Edit the graphit.conf (/usr/local/etc/mars_importer/graphit.conf) and provide information and credentials to connect to a HIRO 6 instance. 

Navigate to the directory containing the MARS JSON definition files and run the importer or provide the absolute path to the source directory as an argument. 

```bash
mars_importer

Usage:
    mars_importer [options] source <source_dir>
    mars_importer [options]

Options:
  --config=CONFIG   Use this config file [default: /usr/local/etc/mars_importer/graphit.conf]
  --timeout=SEC     Set HTTP read timeout [default: 300]
```



License
-----

This tool is licensed under the MIT license: https://opensource.org/licenses/MIT
