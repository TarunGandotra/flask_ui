import tika
from tika import parser
from bs4 import BeautifulSoup
import re
import docx


def ack002(file_xml, file_docx):
    rule_err=[]
    error=[]
    count = 0
    lst=[]
    try:
        with open (file_xml,'r',encoding ='utf-8') as f:
            contents = f.read()
            soup1 = BeautifulSoup(contents,"lxml")
            for i in soup1.findAll("ce:acknowledgment"):
                #print(i.text)
                for j in i.findAll("ce:grant-sponsor"):
                        lst.append(j.text)
                for k in i.findAll("ce:grant-number"):
                        lst.append(k.text)
        #print(lst)
        rawText=parser.from_file(file_docx)
        #print(doc)
        rawList=rawText['content'].splitlines()
        rawlist_join = ' '.join(rawList)
        #print(rawlist_join)
        for substring in lst:
            if substring in rawlist_join:
                continue
            else:
                error.append([contents.index(substring),"funding bodies (grant sponsors and grant numbers)"])
        if error!=[]:
            for i in error:
                rule_file=[]
                rule_file.append("ACK002")
                rule_file.append('Acknowledgment')
                rule_file.append("Important information such as acknowledgement of funding bodies (grant sponsors and grant numbers)")
                rule_file.append("failed")
                rule_file.append(i[0])
                rule_file.append(i[1])
        else:
             rule_file=[]
             rule_file.append("ACK002")
             rule_file.append("Acknowledgment")
             rule_file.append('Important information such as acknowledgement of funding bodies (grant sponsors and grant numbers)')
             rule_file.append("no error")
             rule_err.append(rule_file)
    except Exception as e:
        rule_file=[]
        rule_file.append("ACK002")
        rule_file.append("Acknowledgment")
        rule_file.append('Important information such as acknowledgement of funding bodies (grant sponsors and grant numbers)')
        rule_file.append("no error")
        rule_err.append(rule_file)
    return rule_err      
            #print('error')

##file_jss =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/APCATA_110.docx'
##file_xml =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
##print(ack002(file_xml,file_jss))
