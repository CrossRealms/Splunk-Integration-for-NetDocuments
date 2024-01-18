# NetDocuments App for Splunk

### Download from Splunkbase
https://splunkbase.splunk.com/app/7198/


OVERVIEW
--------
The NetDocuments App for Splunk is a Splunk App that shows the data collected from NetDocuments. It contains useful dashboards.

The App is using data collected by the <a href="https://splunkbase.splunk.com/app/7197/">NetDocuments Add-on for Splunk</a>.


* Author - CrossRealms International Inc.
* Compatible with:
   * Splunk Enterprise version: 9.1, 9.0, 8.2
   * OS: Platform Independent
   * Browser: Google Chrome, Mozilla Firefox, Safari



TOPOLOGY AND SETTING UP SPLUNK ENVIRONMENT
------------------------------------------
This app can be set up in two ways: 
  1. Standalone Mode: 
     * Install the `NetDocuments App for Splunk`.
  2. Distributed Mode: 
     * Install the `NetDocuments App for Splunk` on the search head.
     * App do not require on the Indexer or on the forwarder.


DEPENDENCIES
------------------------------------------------------------
* The App does not have any external dependencies.


INSTALLATION
------------------------------------------------------------
The NetDocuments App needs to be installed only on the Search Head.  

* From the Splunk Web home screen, click the gear icon next to Apps.
* Click on `Browse more apps`.
* Search for `NetDocuments App for Splunk` and click Install. 
* Restart Splunk if you are prompted.


DATA COLLECTION & CONFIGURATION
------------------------------------------------------------
### Update Macro Configuration

1. Log in as administrator and select Settings > Advance search > Search Macros. 
2. Select `NetDocuments App for Splunk (NetDocuments_App)` in the App drop-down. A list of available macros is displayed. 
3. Select and edit the macro and change the definition of macros with new value.


| Macro Name | Description |
| --- | --- |
| netdocs_index | By default, the index name is `netdocs` in the App. But if you have change the index of data from the `NetDocuments Add-on for Splunk` then you have to update the macro definition. |
| netdocs_userlogs_filter |  Update the macro to filter specific user logs events from the dashboard |
| netdocs_adminlogs_filter | Update the macro to filter specific admin logs events from the dashboard |



UNINSTALL APP
-------------
To uninstall app, user can follow below steps:
* SSH to the Splunk instance.
* Go to folder apps($SPLUNK_HOME/etc/apps).
* Remove the `NetDocuments_App` folder from `apps` directory.
* Restart Splunk.


RELEASE NOTES
-------------

Version 1.0.0 (Jan 2024)
* Created Admin Logs and User Logs dashboard.



SAVED-SEARCHES
---------------
* Nothing yet


LOOKUPS
-------
* Nothing yet


OPEN SOURCE COMPONENTS AND LICENSES
------------------------------
* N/A


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
* Copyright - Copyright CrossRealms Internationals, 2024
