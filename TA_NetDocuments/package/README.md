# NetDocuments Add-on for Splunk

### Download from Splunkbase
https://splunkbase.splunk.com/app/7197/


OVERVIEW
--------
The NetDocuments Add-on for Splunk is a Splunk App that allows users to collect Repository Administrator Logs and Repository User Logs from NetDocuments into Splunk. It consists of python scripts to collect the data alongside configuration pages in UI to configure the data collection.

Use the <a href="https://splunkbase.splunk.com/app/7198/">NetDocuments App for Splunk</a> to view the data on the dashboards.

* Author - CrossRealms International Inc.
* Compatible with:
   * Splunk Enterprise version: 9.4, 9.3, 9.2, 9.1, 9.0, 8.2
   * OS: Platform Independent
   * Browser: Google Chrome, Mozilla Firefox, Safari


TOPOLOGY AND SETTING UP SPLUNK ENVIRONMENT
------------------------------------------
This app can be set up in two ways: 
  1. Standalone Mode: 
     * Install the `NetDocuments Add-on for Splunk`.
  2. Distributed Mode: 
     * Install the `NetDocuments Add-on for Splunk` on the search head. The Add-on configuration is not required on the search head.
     * Install the `NetDocuments Add-on for Splunk` on the heavy forwarder. Configure the Add-on to collect the required information from the NetDocuments on the heavy forwarder.
     * The Add-on do not support universal forwarder as it requires python modular inputs to collect the data from NetDocuments.
     * The Add-on do not require on the Indexer.


DEPENDENCIES
------------------------------------------------------------
* The Add-on does not have any external dependencies if you want to collect data from NetDocuments.



INSTALLATION
------------------------------------------------------------
The NetDocuments Add-on needs to be installed on the Search Head and heavy forwarder.  

* From the Splunk Web home screen, click the gear icon next to Apps. 
* Click on `Browse more apps`.
* Search for `NetDocuments Add-on for Splunk` and click Install. 
* Restart Splunk if you are prompted.



### Configure Account ###
* Navigate to `NetDocuments Add-on for Splunk` > `Configuration` > `Account` on Splunk UI.
* Click on `Add`.
* Add below parameters:

| Parameter | Description |
| --- | --- |
| Account name | Any unique name to distinguish this client-id and secret from other in case of multiple accounts configured in the Add-on. |
| Region |  Select region from the dropdown menu. |
| Client Id | Client id received from NetDocuments. |
| Client Secret | Client secret received from NetDocuments. |
| Scope | Select required scope from dropdown menu. |
| Repository ID | Repository ID for which data needs to be collected. |

* Click on `Add`.


### Configure Data Input ###
* Navigate to `NetDocuments Add-on for Splunk` > `Input` on Splunk UI.
* Click on `Create New Input`.
* Select from "Repository Administrator Logs" and "Repository User Logs"
* Add below parameters:

| Parameter | Description |
| --- | --- |
| Name | An unique name for the Input. |
| Interval | Interval in seconds, at which the Add-on should collect latest data from NetDocuments API. Ideal value is between 300 (5 minutes) to 14400 (4 hour). |
| Account to use | Select the account name configured in the Configuration page, which you want to use for data collection. |
| Index | Select/Type the index name in which NetDocuments data will be stored in Splunk. The index name by default supported by `NetDocuments App for Splunk` is `netdocs`. |

* Click on `Save`.



UNINSTALL APP
-------------
To uninstall app, user can follow below steps:
* SSH to the Splunk instance.
* Go to folder apps($SPLUNK_HOME/etc/apps).
* Remove the `TA_NetDocuments` folder from `apps` directory.
* Restart Splunk.


RELEASE NOTES
-------------
Version 1.2.0 (Feb 2026)
* All dependency update. Rebuild App with UCC.
* UCC additional_packaging.py added for better python code structure and improved packaging.

Version 1.1.0 (Jan 2025)
* Rebuild the TA with UCC to upgrade the python libraries.

Version 1.0.1 (Dec 2024)
* Rebuild the TA with UCC to upgrade the python libraries.

Version 1.0.0 (Jan 2024)
* Created Add-on by UCC Splunk-Python library.
* Added Add-on configuration and input pages.



OPEN SOURCE COMPONENTS AND LICENSES
------------------------------
* The Add-on is built by UCC framework (https://pypi.org/project/splunk-add-on-ucc-framework/).


CONTRIBUTORS
------------
* Vatsal Jagani
* Mahir Chavda
* Hardik Dholariya


SUPPORT
-------
* Contact - CrossRealms International Inc.
  * US: +1-312-2784445
* License Agreement - https://cdn.splunkbase.splunk.com/static/misc/eula.html
* Copyright - Copyright CrossRealms Internationals, 2025
