python downloadFileList.py
/u01/app/oracle/middleware/oracle_common/common/bin/wlst.sh downloadFiles.py
zip -rj /u01/data/exportComposite/exportJars/exportJars.zip /u01/data/exportComposite/exportJars
rm /u01/data/exportComposite/exportJars/*.jar
