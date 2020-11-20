
import os
import sys
from bs4 import BeautifulSoup
import re
import logging

def cross_ref(filepath,label):
    lid = label.split()[-1]
    content1 = open(filepath,'r',encoding='utf-8').read()
    soup2 = BeautifulSoup(content1, 'xml')
    soup3 = str(soup2)
    cross_refs = soup2.find_all('cross-ref')
    l=[]
    for j in cross_refs:
        if j.text == '':
            continue
        elif (j['refid'] == lid):
            if j.text == " ".join((label).split()[:-1]):
                continue
            if (j.text == label.split()[-2]):
                continue
            if (j.text == " ".join((label).split()[:-1]).replace(label.split()[-2], ('(' + label.split()[-2] + ')'))):
                continue
            if ((j.text).isalpha()):
                if (j.text == label.split()[-2][-1]):
                    continue
            if ((j.text in " ".join((label).split()[:-1]))):
                if (((j.text).split()[-1]).isdigit() and (j.text).split()[-1] == label.split()[-2][:-1]):
                    index = soup3.index(j.text)
                    l = ['BRX018',"Bibliographic reference cross-references","in the text citations between bibliographic references that have the same author/group of authors and the same year","error",str(index),"Suffix Missing"]
    return l


def BRX018(filepath,jsspath):
    labels = []
    name_date = []
    final = []
    try:
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
                    name_date.append((name + " " + label_date))
                else:
                    name_date.append((name[:-1] + " " + label_date))
            
            dups = list(set([x for x in name_date if name_date.count(x) > 1]))
            
            if dups !=[]:
                for k in dups:
                    fn = k.split()[0]
                    sn = k.split()[-2]
                    yr = k.split()[-1]
                    l=[]
                    for s in labels:
                        if ((yr in s) and (sn in s)):
                            if ((re.findall('.*([1-3][0-9]{3}[a-z])', s) !=[]) and s[-9].isalpha()):
                                d = cross_ref(filepath,s)
                                if d !=[]:
                                    final.append(d)
                            else:
                                l.append(s[:-8])
                    
                    dup1 = list(set([x for x in l if l.count(x) > 1]))
                    
                    if dup1 != []:
                        for a in l:
                            index = soup1.index(a)
                            d = ["BRX018","Bibliographic reference cross-references","in the text citations between bibliographic references that have the same author/group of authors and the same year","error",str(index),"Suffices not present in the label"]
                            final.append(d)
                    
                if final == []:
                    d = ["BRX018","Bibliographic reference cross-references","in the text citations between bibliographic references that have the same author/group of authors and the same year","no error"]
                    final.append(d)
            else:
                d = ["BRX020A","Bibliographic reference cross-references","in the text citations between bibliographic references that have the same author/group of authors and the same year","no error"]
                final.append(d)
        else:
            d = ["BRX020A","Bibliographic reference cross-references","in the text citations between bibliographic references that have the same author/group of authors and the same year","no error"]
            final.append(d)
        return final
    except Exception as e:
        final = []
        d = ['BRX018','Bibliographic reference cross-references','in the text citations between bibliographic references that have the same author/group of authors and the same year','no error']
        final.append(d)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX018 : Bibliographic reference cross-references " )
        logging.shutdown()
        return final

# file_jss =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/APCATA-jss.xml'
# file_xml =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
# print(BRX018(file_xml,file_jss))
