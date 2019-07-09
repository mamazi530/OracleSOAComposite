import sys
import pickle
import os

def save_list_file():

    
    # f = os.popen("java weblogic.WLST /u01/data/exportComposite/listComposites.py")
    f = os.popen("/u01/app/oracle/middleware/oracle_common/common/bin/wlst.sh /u01/data/exportComposite/listComposites.py")
    #f = os.popen("C:/Oracle/Soa12.1.3.0/oracle_common/common/bin/wlst.cmd D:/vscodeProject/PythonTest/listComposites.py")
    now = f.read()
    file = open("/u01/data/exportComposite/compositesList.txt","w+")
    file.write("This : %s\r\n" % now)    
   

save_list_file()
