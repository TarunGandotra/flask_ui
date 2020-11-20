import os
import sys
from bs4 import BeautifulSoup
import re
import logging

def BRX019(filepath,jsspath):
    try:
        sname_date = []
        labels = []
        final = []
        jss = open(jsspath,"r",encoding="utf-8")
        soup = BeautifulSoup(jss,'xml')
        string = ""
        k = soup.find_all('refStyle')
        string = k[0].text
        if (string[0].isdigit() and (string[0] in ['2','4','5','7','8','9b'])):
            content = open(filepath,'r',encoding='utf-8').read()
            soup = BeautifulSoup(content, 'xml')
            soup1 = str(soup)
            bib_refs = soup.find_all('bib-reference')
            l=[]
            for j in bib_refs:
                label = j.find_all('label')[0].text
                sb_ref = j.find_all('reference')
                other_ref = j.find_all('other-ref')
                if sb_ref !=[]:
                    if sb_ref[0].find_all('date') !=[]:
                        date = sb_ref[0].find_all('date')[0].text
                        if ((re.findall('.*([1-3][0-9]{3}[a-z])', label) !=[]) and label[-1].isalpha()):
                            if date.isdigit():
                                continue
                            else:
                                index = soup1.index(date)
                                l = ["BRX019","Bibliographic reference cross-references","for references structured with the sb:reference element do not add the 'a', 'b' suffixes to the content of the ce:date elements","Error",str(index),"Suffix absent"]
                                final.append(l)
                elif other_ref !=[]:
                    if ((re.findall('.*([1-3][0-9]{3}[a-z])', label) !=[]) and label[-1].isalpha() and (re.findall('.*([1-3][0-9]{3}[a-z])', other_ref[0].find_all('textref')[0].text) !=[])):
                        continue
                    elif ((re.findall('.*([1-3][0-9]{3}[a-z])', label) !=[]) and label[-1].isdigit()):
                        index = soup1.index(label)
                        l = ["BRX019","Bibliographic reference cross-references""for references structured with the sb:reference element do not add the 'a', 'b' suffixes to the content of the ce:date elements","Error",str(index),"Suffix not present in label, (ce:other-ref) case"]
                        final.append(l)
                    elif (re.findall('.*([1-3][0-9]{3}[a-z])', other_ref[0].find_all('textref')[0].text) !=[]):
                        index = soup1.index(label)
                        l = ["BRX019","Bibliographic reference cross-references","for references structured with the sb:reference element do not add the 'a', 'b' suffixes to the content of the ce:date elements","Error",str(index),"Suffix not present with date in the manually formatted content, (ce:other-ref case)"]
                        final.append(l)
            if final == []:
                l = ["BRX019","Bibliographic reference cross-references","for references structured with the sb:reference element do not add the 'a', 'b' suffixes to the content of the ce:date elements","no error"]             
                final.append(l)
        else:
            l = ["BRX019","Bibliographic reference cross-references","for references structured with the sb:reference element do not add the 'a', 'b' suffixes to the content of the ce:date elements","no error"]             
            final.append(l)
        return final
    except Exception as e:
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX019 : Bibliographic reference cross-references " )
        logging.shutdown()
        l = ["BRX019","Bibliographic reference cross-references","for references structured with the sb:reference element do not add the 'a', 'b' suffixes to the content of the ce:date elements","no error"]             
        final.append(l)
        return final
