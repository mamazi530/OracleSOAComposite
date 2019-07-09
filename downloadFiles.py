import time


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

file = open('/u01/data/exportComposite/compositesList.txt','r+')
exportLogFile = open("/u01/data/exportComposite/exportLogs/exportlog"+time.strftime("%Y-%m-%d"+"_"+"%H:%M:%S", time.localtime())+".txt",'w+')
#exportLogFile.writelines('host : '+host+' || path : '+path+' || username : '+username+' || pwd : '+pwd+'\n')
for lines in file:
	line = lines.split(',')
	exportLogFile.writelines(line)
	if len(line)> 6:
		absName = line[0].split()[1]
		fileName = absName[0:absName.find('[')]
		version = absName[absName.find('[')+1:len(absName)-1]
		partition=line[1].split('=')[1]
		#exportLogFile.writelines('absName : '+absName+' || fileName : '+fileName+' || version : '+version+' || partition : '+partition+'\n')
		if partition == 'default':
			exportLogFile.writelines('host : '+host+' || path : '+path+'sca_'+fileName+'_rev'+version+'.jar'+' || fileName : '+fileName+' || version : '+version+' || partition : '+partition +' || username : '+username+' || pwd : '+pwd+'\n')
			sca_exportComposite(host,"all",path+'sca_'+fileName+'_rev'+version+'.jar',fileName,version,user=username,password=pwd,partition=partition)
