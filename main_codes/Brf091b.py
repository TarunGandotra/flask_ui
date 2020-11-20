from bs4 import BeautifulSoup
import re
import logging
def BRF091B(file_xml,file_jss):

    try: 
        with open(file_xml,'r',encoding ='utf-8') as f:              
            contents = f.read()
            count = 0
            rule_err = []
            error = []
            list1=[]
            listj=[]
            list_ACS=[]
            listi =['Available from:','Retrieved from','Published online:']
            list_van=['3 Vancouver numbered','3a Embellished Vancouver','4 Vancouver name/year']
            soup = BeautifulSoup(contents,'lxml')
            for i in soup.find_all('ce:bibliography'):
                for j in i.find_all('sb:comment'):
                    #print(j.text)
                    listj.append(j.text)
            #print(listj,'hhdju')

            for i in listj:
                for j in listi:
                    if i==j:
                        list1.append(i)
                    else:
                        pass
   
            with open(file_jss,'r',encoding ='utf-8') as f1:


                contents1 = f1.read()
                count = 0

                styleName=[]

                soup = BeautifulSoup(contents1,'lxml')
                for i in soup.find_all('refstyle'):
                    #print(i.text)
                    styleName.append(i.text)


                
                if styleName[0]=='5 APA':
                   # print('APA')
                    for i in list1:
                        #print(i,'146566')
                        if i == 'Retrieved from':
                            pass
                        else:

                            error.append([str(contents.index(i)),"ce:commend tag must according to style"])
                elif styleName[0]=='ACS':
                   # print('ACS')
                    for i in list1:
                        #print(i,'146566')
                        if i == 'Published online:':
                            pass
                        else:
                            error.append([str(contents.index(i)),"ce:commend tag must according to style"])
                elif styleName[0] in list_van:
                   # print('VAN')
                    for i in list1:
                        #print(i,'146566')
                        if i == 'Available from:':
                            pass
                        else:
                            error.append([str(contents.index(i)),"ce:commend tag must according to style"])
                else:
                    a =0+0
                    #print('no error')
        if error!=[]:
                for err in error:
                    rule_file=[]
                    rule_file.append("BRF091B")
                    rule_file.append("Bibliographic references")
                    rule_file.append("ce:commend tag is not according to style")
                    rule_file.append("failed")
                    rule_file.append(err[0])
                    rule_file.append(str(err[1]))
                    rule_err.append(rule_file)
        else:
                rule_file=[]
                rule_file.append("BRF091B")
                rule_file.append("Bibliographic references")
                rule_file.append("ce:commend tag is according to style")
                rule_file.append("no error")
                rule_err.append(rule_file)
    except Exception as e:
        rule_file=[]
        rule_file.append("BRF091B")
        rule_file.append("Bibliographic references")
        rule_file.append("ce:commend tag is according to style")
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRF091B : Bibliographic references " )
        logging.shutdown()

    return rule_err
# file_xml=r'E:\test\COLEGN_607----Rule no. BRF020A, BRF027, BRF028, BRF034, BRF037A, BRF032A\tx1.xml'
# file_jss=r'E:\test\COLEGN_607----Rule no. BRF020A, BRF027, BRF028, BRF034, BRF037A, BRF032A\COLEGN-jss.xml'
# print(BRF091B(file_xml,file_jss))
