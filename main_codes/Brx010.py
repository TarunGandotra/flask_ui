import os
import sys
from tika import parser

def BRX010(filepath,jsspath):
    try:
        
        final = []
        jss = open(jsspath,"r",encoding="utf-8")
        soup = BeautifulSoup(jss,'xml')
        string = ""
        k = soup.find_all('refStyle')
        string = k[0].text
        if (string[0].isdigit() and (string[0] in ['2','4','5','7','8','9b'])):
            file = open(filepath,'r',encoding='utf-8').read()
            soup1 = BeautifulSoup(file, 'xml')
            soup2 = str(soup1)
            bib_refs = soup1.find_all('bib-reference')
            a={}
            for j in bib_refs:
                label = j.find_all('label')[0].text
                sname = j.find_all('surname')
                sb_ref = j.find_all('reference')
                lid = j['id']
                if sb_ref !=[] and sb_ref[0].find_all('date') !=[]:
                    date = sb_ref[0].find_all('date')[0].text
                matches = [x.text for x in sname if x.text in label]
                if len(matches) > 1:
                    matches.append(date)
                    a[lid] = " ".join(matches)
            
            d={}
            for key,value in a.items():
                d.setdefault(value,set()).add(key)
            
            l = list(set(chain.from_iterable(values for key, values in d.items() if len(values) > 1)))
            
            if l != []:
                f=[]
                for i in l:
                    cross_ref = soup1.find_all('cross-ref', refid = i)[0].text
                    fnames = soup1.find_all('bib-reference', id = i)[0].find_all('given-name')
                    b=[]
                    
                    for j in fnames:
                        b.append(j.text)
                    
                    if len([x for x in b if x in cross_ref]) > 1:
                        continue
                    elif len([x for x in b if x in cross_ref]) == 1:
                        index = soup2.index(cross_ref)
                        f = ["BRX010","jid","aid","Error",str(index),"First Names of some authors are missing!"]
                        final.append(f)
                    elif len([x for x in b if x in cross_ref]) == 0:
                        index = soup2.index(cross_ref)
                        f = ["BRX010","jid","aid","Error",str(index),"First Names of all authors are missing!"]
                        final.append(f)
                
                if final == []:
                    f = ["BRX010","Bibliographic reference cross-references","the phrase 'and co-workers' in journals with numbered reference styles is acceptable if an author has used it in citing multiple references","no error"]
                    final.append(f)
            else:
                f = ["BRX010","Bibliographic reference cross-references","the phrase 'and co-workers' in journals with numbered reference styles is acceptable if an author has used it in citing multiple references","no error"]
                final.append(f)
        
        else:
            f = ["BRX010","Bibliographic reference cross-references","the phrase 'and co-workers' in journals with numbered reference styles is acceptable if an author has used it in citing multiple references","no error"]
            final.append(f)
        
        return final
    
    except Exception as e:
        final = []
        f = ["BRX010","Bibliographic reference cross-references","the phrase 'and co-workers' in journals with numbered reference styles is acceptable if an author has used it in citing multiple references","no error"]
        final.append(f)
        
        return final
