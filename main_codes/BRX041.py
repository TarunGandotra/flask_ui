import re
import os
import sys
from bs4 import BeautifulSoup
import logging
def brx041(path):
    List1=[]
    try:
        infile = open(path,"r",encoding="utf8")
        soup=BeautifulSoup(infile,'lxml')
        soup1=str(soup)
        abstract=soup.find_all('ce:abstract')
        text=[item.get_text() for item in abstract]
        if(len(text)>0):
            abs_text=""
            for chars in text:
                abs_text=abs_text+chars
            main=soup.find_all('ce:sections')
            text2=[item.get_text() for item in main]
            main_text=""
            for chars in text2:
                main_text=main_text+chars
            reference=soup.find_all('ce:bibliography')
            text1=[item.get_text() for item in reference]
            string=""
            for chars in text1:
                string=string+chars
            ref=string.split('[')
            for ind,item in enumerate(ref):
                if(item[:-1]!="Reference"):
                    if(']' in item):
                        ref[ind]=item[item.index(']')+1:]

            for i in range(len(abs_text)):
                s=""
                mnop=0
                if abs_text[i]=="[":
                    s=s+'[';
                    for ind in range(i+1,len(abs_text)):
                        s=s+abs_text[ind]
                        if(abs_text[ind]==']'):
                            break
                    if s not in main_text:
                        lis1=re.findall('[a-zA-z]+\s',s)

                        if(len(lis1)!=0):
                            ih=soup1.index(s)
                            List1.append(["BRX041","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and not cited anywhere else in the main body of the text replace the citation","error",str(ih),"Error:Sholud be replaced with name-date numbered cross-reference"])
                        else:
                            lis2=re.findall('[a-zA-Z]+\s\(\d\d\d\d\)\s\[\d+\]',abs_text[:ind+1])
                            if len(lis2)>0: 
                                l1=lis2[-1]
                                for references in ref:
                                    if s1 in references:
                                        mnop=1
                                if(mnop==0):
                                    ih=soup1.index(s)
                                    List1.append(["BRX041","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and not cited anywhere else in the main body of the text replace the citation","error",str(ih),"ERROR:name date numbered cross reference not in References"])
                            else:
                                ih=soup1.index(s)
                                List1.append(["BRX041","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and not cited anywhere else in the main body of the text replace the citation","error",str(ih),"Error:citation shold be replaced with name date and numbered cross ref"])
        if len(List1)==0:
            List1.append(["BRX041","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and not cited anywhere else in the main body of the text replace the citation","no error"])
        return List1
    except Exception as e:
        List2=[]
        List2.append(["BRX041","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and not cited anywhere else in the main body of the text replace the citation","no error"])
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX041 : Bibliographic reference cross-references " )
        logging.shutdown()
        return List2

#file_xml =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(brx041(file_xml))
