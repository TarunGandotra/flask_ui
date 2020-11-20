import os
import sys
from bs4 import BeautifulSoup
import re
import logging

def surname(filepath,label):
    lid = label.split()[-1]
    content = open(filepath,'r',encoding='utf-8').read()
    soup = BeautifulSoup(content, 'xml')
    soup1 = str(soup)
    cross_refs = soup.find_all('cross-ref')
    for j in cross_refs:
        if j.text == '':
            l=[]
            continue
        elif (j['refid'] == lid and j.text == " ".join((label).split()[:-1])):
            fname = soup.find_all('ce:bib-reference',id = j['refid'])[0].find_all('ce:given-name')[0].text
            if fname in j.text:
                l=[]
                continue
        elif (j['refid'] == lid and j.text == " ".join((label).split()[1:-1])):
            fname = soup.find_all('ce:bib-reference',id = j['refid'])[0].find_all('ce:given-name')[0].text
            if fname not in j.text:
                index = soup1.index(j.text)
                l = ['BRX020A',"Bibliographic reference cross-references","the bibliographies contain different references with different first authors but who share the same surname, and where the date of publication is the also the same","error",str(index),"First name missing in cititaion"]
    return l

def BRX020A(filepath,jsspath):
    
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
            soup1 = BeautifulSoup(content, 'lxml')
            bib_refs = soup.find_all('ce:bib-reference')
            for j in bib_refs:
                label = j.find_all('label')[0].text
                fname = j.find_all('given-name')
                sname = j.find_all('surname')
                bib_id = j['id']
                if (fname != [] and sname!= []):
                    name = (fname[0].text + ' ' + sname[0].text)
                elif (fname == [] and sname!= []):
                    name = sname[0].text.replace(" ", "-")
                elif (fname != [] and sname == []):
                    name = fname[0].text.replace(" ", "-")
                sb_ref = j.find_all('reference')
                if sb_ref !=[] and sb_ref[0].find_all('date') !=[]:
                    label_date = sb_ref[0].find_all('date')[0].text
                labels.append(label + " " + bib_id)
                if name[-1].isalpha():
                    sname_date.append(((name.split()[-1]) + " " + label_date))
                else:
                    sname_date.append(((name.split()[-1][:-1]) + " " + label_date))
            
            sdups = list(set([x for x in sname_date if sname_date.count(x) > 1]))
            
            if sdups !=[]:
                for k in sdups:
                    sub1 = k.split()[-2]
                    sub2 = k.split()[-1]
                    l=[]
                    for t in labels:
                        if ((sub1 in t) and (sub2 in t)):
                            if ((t not in l) and (re.findall('.*([1-3][0-9]{3}[a-z])', t) ==[]) and (t[-9].isdigit()) and (re.findall('.*([1-3][0-9]{3})', t) != [])): 
                                d = surname(filepath,t)
                                if d!=[]:
                                    final.append(d)
                            elif ((t not in l) and (re.findall('.*([1-3][0-9]{3}[a-z])', t) !=[]) and (t[-9].isalpha())):
                                continue
                    if final == []:
                        d = ["BRX020A","Bibliographic reference cross-references","the bibliographies contain different references with different first authors but who share the same surname, and where the date of publication is the also the same","no error"]
                        final.append(d)
            else:
                d = ["BRX020A","Bibliographic reference cross-references","the bibliographies contain different references with different first authors but who share the same surname, and where the date of publication is the also the same","no error"]
                final.append(d)
        else:
            d = ["BRX020A","Bibliographic reference cross-references","the bibliographies contain different references with different first authors but who share the same surname, and where the date of publication is the also the same","no error"]
            final.append(d)
        return final
    
    except Exception as e:
        final = []
        d = ['BRX011','Bibliographic reference cross-references','the bibliographies contain different references with different first authors but who share the same surname, and where the date of publication is the also the same','no error']
        final.append(d)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX011 : Bibliographic reference cross-references " )
        logging.shutdown()
        return final

