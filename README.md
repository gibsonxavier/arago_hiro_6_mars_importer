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
## Organization
Please ensure that the ogit/organization with the value used in the cusotmerID field of the excel exsts, else please create it using:

URL to POST the request:
```bash
 https://hiro_instance/new/ogit%2FOrganization
 
 Send header _TOKEN=$TOKEN
```
JSON Payload: 
```java
 {
    "ogit/_graphtype" : "vertex",
    "ogit/_is-deleted" : "false",
    "ogit/_type" : "ogit/Organization",
    "ogit/_xid" : "ORGANIZATION",
    "ogit/description" : "ORGANIZATION",
    "ogit/name" : "ORGANIZATION"
  }
```
Python code:
```python
import requests

url = "https://HOSTNAME/new/ogit%2FOrganization"

payload = " {\n    \"ogit/_graphtype\" : \"vertex\",\n    \"ogit/_is-deleted\" : \"false\",\n    \"ogit/_type\" : \"ogit/Organization\",\n    \"ogit/_xid\" : \"ORGANIZATION\",\n    \"ogit/description\" : \"ORGANIZATION\",\n    \"ogit/name\" : \"ORGANIZATION\"\n  }"
headers = {
    '_TOKEN': TOKEN,
    'Content-Type': "application/json",
    }
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
````
## Authentication Errors (403)
In case of authentication or access denied errors, please check the client being used. What should always work is the client for Local data load: (HIRO LocalDataLoad-Inital data load for HIRO GraphDB)

License
-----

This tool is licensed under the MIT license: https://opensource.org/licenses/MIT
