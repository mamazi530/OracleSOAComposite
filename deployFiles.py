import os
import time

def fileRead(dirPath):
    infoFile = open('/u01/data/exportComposite/soaInfo.txt','r+')
    for infoLines in infoFile:
        infoline = infoLines.strip('\n').split('=')
        if infoline[0] == 'host' :
            host = infoline[1] 
        elif infoline[0] == 'path' :
            path = infoline[1] 
        elif infoline[0] == 'username' :
            username =  infoline[1] 
        elif infoline[0] == 'pwd' :
            pwd =  infoline[1] 
        elif infoline[0] == 'partition' :
            partition =  infoline[1]
	elif infoline[0] == 'configplan' :
            configplan = infoline[1] 
	elif infoline[0] == 'overwrite' :
            overwrite = infoline[1] 

    deployLogFile = open("/u01/data/exportComposite/importLogs/importlog"+time.strftime("%Y-%m-%d"+"_"+"%H:%M:%S", time.localtime())+".txt",'w+')
    for file in os.listdir(dirPath) :
        if file.endswith('.jar') :            
		if configplan != '' and os.path.exists(configplan) :
			sca_deployComposite(host,dirPath+'/'+file,overwrite=overwrite=='true',user=username,password=pwd,configplan=configplan,partition=partition)
			deployLogFile.writelines('host : '+host+' || path : '+dirPath+'/'+file +' || configplan :+'+configplan+' || partition :+'+partition+' || file :'+file +' || overwrite :'+overwrite +'\n')
		else:
            		sca_deployComposite(host,dirPath+'/'+file,overwrite=overwrite=='true',user=username,password=pwd,partition=partition)
            		deployLogFile.writelines('host : '+host+' || path : '+dirPath+'/'+file +' || partition :+'+partition+' || file :'+file+' || overwrite :'+overwrite +'\n') 
     
   

fileRead('/u01/data/exportComposite/importJars')
