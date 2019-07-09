# OracleSOAComposite
The Script to export and import SOA Composites (writed by python)


1. soaInfo used as a config file with the info login SOA server.
2. do not modify the dirs structure.

##Usage
1.import all file to the vm under /u01/data/exportComposite
2.Change the soaInfo to your SOA server info
3.Change the listComposites to your SOA server info
4.when export, the compositesList.txt will get the composites list
5.all export composites will be zip in the exportJars and log will be in exportLogs
6.when import, need to upload all composites to importJars(not zip) and log will be in importLogs
