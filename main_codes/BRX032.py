import os
import re
import logging
from bs4 import BeautifulSoup

def brx032(pathxml,pathjss):
    try:
        injss=open(pathjss,'r',encoding="utf8")
        soup2=BeautifulSoup(injss,'xml')
        refsty=soup2.find_all('refStyle')
        for ite in refsty:
            if ite.get_text()=="":
                return [["BRX032","Bibliographic reference cross-references","text citations in styles other than those detailed in the examples above","no error"]]
            elif ite.get_text()=="5 APA" or ite.get_text()=="2 Harvard":
                Lst=[]
                infile=open(pathxml,'r',encoding='utf-8')
                soup=BeautifulSoup(infile,'lxml')
                soup3=str(soup)
                l=soup.find_all("ce:cross-ref")
                l1=[]
                for tags in l:
                    if(tags['refid'][:3]=="bib"):
                        l1.append(tags.text)
                for refs in l1:
                    if ' colleague' in refs or ' co-worker' in refs or " coworker" in refs:
                        indices=soup3.index(refs)
                        Lst.append(["BRX032","Bibliographic reference cross-references","text citations in styles other than those detailed in the examples above","error",str(indices),"Error:colleague or co-worker should not appear in text citation for 5 APA and 2 Harvard"])
                if(len(Lst)==0):
                    Lst.append(["BRX032","Bibliographic reference cross-references","text citations in styles other than those detailed in the examples above","no error"])
                return Lst
            else:
                return [["BRX032","Bibliographic reference cross-references","text citations in styles other than those detailed in the examples above","no error"]]
    except Exception as e:
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX032 : Bibliographic reference cross-references " )
        logging.shutdown()
        List25=[]
        List25.append(["BRX032","Bibliographic reference cross-references","text citations in styles other than those detailed in the examples above","no error"])
        return List25

# file_jss =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/APCATA-jss.xml'
# file_xml =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
# print(brx032(file_xml,file_jss))
