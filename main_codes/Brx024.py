import os
import sys
from bs4 import BeautifulSoup
import re
import logging

def BRX024(filepath,jsspath):
    try:
        sname_date = []
        labels = []
        final = []
        jss = open(jsspath,"r",encoding="utf-8")
        soup = BeautifulSoup(jss,'xml')
        string = ""
        k = soup.find_all('refStyle')
        string = k[0].text
        if (string[0].isdigit() and (string[0] in ['2','4','7','8','9b'])):
            content = open(filepath,'r',encoding='utf-8').read()
            soup = BeautifulSoup(content, 'xml')
            soup1 = str(soup)
            bib_refs = soup.find_all('bib-reference')
            for j in bib_refs:
                sb_ref = j.find_all('reference')
                other_ref = j.find_all('other-ref')
                if sb_ref == []:
                    if other_ref !=[]:
                        text_ref = other_ref[0].find_all('textref')[0].text
                        if (('Anon' in text_ref) or ('ANON' in text_ref) or ('ANNON' in text_ref)):
                            label = j.find_all('label')[0].text
                            lid = j['id']
                            if (('Anon' in label) or ('ANON' in label) or ('ANNON' in label)):
                                cross_refs = soup.find_all('cross-ref')
                                l=[]
                                for k in cross_refs:
                                    if k.text == '':
                                        continue
                                    elif (k['refid'] == lid and k.text == label):
                                        continue
                                    elif (k['refid'] == lid and k.text != label):
                                         if (k.text).isdigit():
                                            index = soup1.index(k.text)
                                            l = ["BRX024","Bibliographic reference cross-references","Where works that have no author are cited in the bibliography, 'Anon' can be added in place of the author","error",str(index),"'Anon' not present!"]
                                            final.append(l)
            if final == []:
                l = ["BRX024","Bibliographic reference cross-references","Where works that have no author are cited in the bibliography, 'Anon' can be added in place of the author","no error"]
                final.append(l)
        else:
            l = ["BRX024","Bibliographic reference cross-references","Where works that have no author are cited in the bibliography, 'Anon' can be added in place of the author","no error"]
            final.append(l)
        return final
    except Exception as e:
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX024 : Bibliographic reference cross-references " )
        logging.shutdown()
        l = ["BRX024","Bibliographic reference cross-references","Where works that have no author are cited in the bibliography, 'Anon' can be added in place of the author","no error"]             
        final.append(l)
        return final
