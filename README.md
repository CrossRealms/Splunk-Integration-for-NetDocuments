# Splunk-Integration-for-NetDocuments

Splunk Add-on and App for NetDocuments Logs


## UCC Document
* [UCC Add-on Quick Start](https://splunk.github.io/addonfactory-ucc-generator/quickstart/)

### UCC Command to Build the Add-on after change
```
ucc-gen build --source TA_NetDocuments --ta-version 1.0.0
cp -r output/TA_NetDocuments/* TA_NetDocuments/
rm -rf TA_NetDocuments/static/openapi.json # To fix App Inspect failure
```
