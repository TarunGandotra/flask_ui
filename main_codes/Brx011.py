
import os
import sys
from bs4 import BeautifulSoup
import re
import logging


def multifind(string, value, start = 0, stop = None):
    values = []
    while True:
        found = string.find(value, start, stop)
        if found == -1:
            break
        values.append(found)
        start = found + 1
    return values

def BRX011(filepath,jsspath):
    
    try:
        final=[]
        jss = open(jsspath,"r",encoding="utf-8")
        soup = BeautifulSoup(jss,'xml')
        string = ""
        k = soup.find_all('refStyle')
        string = k[0].text
        if (string[0].isdigit() and (string[0] in ['1','3','6'])):
            content = open(filepath,'r',encoding='utf-8').read()
            soup1 = BeautifulSoup(content, 'lxml')
            soup2 = str(soup1)
            cross_ref = soup1.find_all('ce:cross-ref')
            cross_refs = soup1.find_all('ce:cross-refs')
            
            list1=[]
            for j in (cross_ref + cross_refs):
                if j['refid'].count('bib') >= 1:
                    l = multifind(soup2,str(j))
                    for k in l:
                        if "Ref." in soup2[k-5:k]:
                            if "Ref." not in (soup1.find_all('ce:bib-reference',id = j['refid'])[0].find_all('ce:label')[0].text):
                                if (j.text).isdigit():
                                    continue
                                elif (re.findall('\[\d+\]',j.text) != []):
                                    continue
                                else:
                                    index = soup2.index(j.text)
                                    list1 = ['BRX011',"Bibliographic reference cross-references","In instances where a reference is mentioned that is cited within a bibliographic reference",'error',str(index),"Wrong Reference, should be numbered only"]
                                    final.append(list1)
                            else:
                                label = soup1.find_all('ce:bib-reference',id = j['refid'])[0].find_all('ce:label')[0].text
                                index = soup2.index(label)
                                list1 = ['BRX011','Bibliographic reference cross-references','In instances where a reference is mentioned that is cited within a bibliographic reference','error',str(index),'Ref. present in the ce:label of target bibliographic reference']
                                final.append(list1)
                        else:
                            continue
            if final == []:
                list1 = ['BRX011','Bibliographic reference cross-references','In instances where a reference is mentioned that is cited within a bibliographic reference','no error']
                final.append(list1)
        else:
            return [['BRX011','Bibliographic reference cross-references','In instances where a reference is mentioned that is cited within a bibliographic reference','no error']]
        return final
    except Exception as e:
	#final-[
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX011 : Bibliographic reference cross-references" )
        logging.shutdown()
        list1 = ['BRX011','Bibliographic reference cross-references','In instances where a reference is mentioned that is cited within a bibliographic reference','no error']
        final.append(list1)
        return final

#jsspath =r'E:\test\JSS\APCATA/APCATA-jss.xml'
#filepath =r'E:\test\MNT_ELSEVIER_JOURNAL_APCATA_17035_110/fs.xml'
#print(BRX011(filepath,jsspath))
