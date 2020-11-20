import os
import sys
from bs4 import BeautifulSoup
import re
import logging

def BRX022(filepath,jsspath):
    
    try:
        
        final=[]
        jss = open(jsspath,"r",encoding="utf-8")
        soup = BeautifulSoup(jss,'xml')
        string = ""
        k = soup.find_all('refStyle')
        string = k[0].text
        if (string[0].isdigit() and (string[0] in ['2','4','5','7','8','9b'])):
            content = open(filepath,'r',encoding='utf-8').read()
            soup1 = BeautifulSoup(content, 'xml')
            soup2 = str(soup1)
            cross_refs = soup1.find_all('cross-refs')
            l=[]
            
            for i in cross_refs:
                
                if i['refid'].count('bib') > 1:
                    l = i['refid'].split()
                    c=0
                    m=[]
                    
                    label_names = []
                    for z in l:
                        label = (soup1.find_all('bib-reference',id=z)[0].find_all('label'))[0].text
                        label_names.append(label[:label.index(',')])
                        
                    dups = list(set([x for x in label_names if label_names.count(x) > 1]))
                    
                    if dups != []:
                        for j in l:
                            comment = (soup1.find_all('bib-reference',id = j)[0].find_all('reference')[0].find_all('comment')[0].text)
                            if "in press" in comment:
                                m.append(comment)
                                c+=1

                        if c == len(l):

                            if (i.text).count("in press") ==  len(l):

                                d=0

                                for k in m:
                                    if k in i.text:
                                        d+=1

                                if d == len(m):

                                    f = ["BRX022","Bibliographic reference cross-references","aid","no error"]
                                    final.append(f)

                                else:
                                    index = soup2.index(i.text)
                                    f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","error",str(index),"Wrong method of citation!"]
                                    final.append(f)
                            else:
                                index = soup2.index(i.text)
                                f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","error",str(index),"Wrong method of citation!"]
                                final.append(f)
                        else:
                            f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","no error"]
                            final.append(f)
                    
                    else:
                        f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","no error"]
                        final.append(f)
                
                else:
                    f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","no error"]
                    final.append(f)
                    
            if final == []:
                f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","no error"]
                final.append(f)
        
        else:
            f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","no error"]
            final.append(f)
        
        return final
    
    except Exception as e:
        #print(e.with_traceback())
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX022 : Bibliographic reference cross-references " )
        logging.shutdown()
        final = []
        f = ["BRX022","Bibliographic reference cross-references","Citation together of different references not yet published and with the same author acc. to style","no error"]
        final.append(f)
        return final
