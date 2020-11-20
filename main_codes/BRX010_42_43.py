import re
from bs4 import BeautifulSoup
import logging

def BRX010_42(file_jss,file_xml):
    rule_err = []
    error = []
    listj =[]
    ref_style1=['1 Numbered','3 Vancouver','3a Embellished Vancouver']
    try:
        with open(file_jss,'r',encoding ='utf-8') as f:
            contents1 = f.read()
        #print(contents[58137:58337])
        soup1 = BeautifulSoup(contents1,'lxml')
        for ref in soup1.find_all('refstyle'):
            refstyle=(ref.text)
        if refstyle in ref_style1:
            with open(file_xml,'r',encoding ='utf-8') as f:
                contents = f.read()
                #print(contents[58137:58337])
                soup = BeautifulSoup(contents,'lxml')
                list_tag=['book-review','article','simple-article']
                count = 0
                for sec in soup.find_all('ce:sections'):
                    for para in sec.find_all('ce:para'):
                        cross_ref=['ce:cross-ref','ce:cross-refs']
                        for tag in para.find_all(cross_ref):
                            #print(tag.attrs['refid'],'???'*20)
                            k=tag.attrs['refid']
                            n= re.findall(r"^bib",k)
                            if bool(n)==True:
                                loc=(contents.index(tag.attrs['id']))
                                str2=contents[loc-50:loc]
                                #print(str2)
                                if 'and co-workers' in str2:
                                    #print(k)
                                    count_bib=k.count('bib')
                                    #print(count_bib)
                                    if count_bib>1:
                                        pass
                                        #print('no error',tag,refstyle)
                                    else:
                                        error.append([str(contents.index(tag.attrs['id'])),'Co-workers use when single reference citation present for numbered reference(Error)'])
        else:
            #print(refstyle)
            with open(file_xml,'r',encoding ='utf-8') as f:
                contents = f.read()
            soup = BeautifulSoup(contents,'lxml')
            list_tag=['book-review','article','simple-article']
            count = 0
            for sec in soup.find_all('ce:sections'):
                for para in sec.find_all('ce:para'):
                    cross_ref=['ce:cross-ref','ce:cross-refs']
                    for tag in para.find_all(cross_ref):
                        k=tag.attrs['refid']
                        n= re.findall(r"^bib",k)
                        if bool(n)==True:
                            loc=(contents.index(tag.attrs['id']))
                            str2=contents[loc-50:loc]
                            #print(str2)
                            if 'co-workers' in str2:
                                error.append([str(contents.index(tag.attrs['id'])),'Co-workers appering befor name date reference citation but it is not allow for name date style'])
        if error!=[]:
            for i in error:
                rule_file=[]
                rule_file.append("BRX010(42-43)")
                rule_file.append('Bibliographic reference cross-references')
                rule_file.append('The phrase "and co-workers" is often used by authors when citing multiple (numbered) references')
                rule_file.append("error")
                rule_file.append(i[0])
                rule_file.append(i[1])
                rule_err.append(rule_file)
        else:
            rule_file=[]
            rule_file.append("BRX010(42-43)")
            rule_file.append("Bibliographic reference cross-references")
            rule_file.append('The phrase "and co-workers" is often used by authors when citing multiple (numbered) references')
            rule_file.append("no error")
            rule_err.append(rule_file)
    except Exception as e:
        print(e)
        rule_file=[]
        rule_file.append("BRX010(42-43)")
        rule_file.append("Bibliographic reference cross-references")
        rule_file.append('The phrase "and co-workers" is often used by authors when citing multiple (numbered) references')
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX010(42-43) : Bibliographic reference cross-references " )
        logging.shutdown()
                    

    return rule_err 
#file_xml=r'C:\Users\digiscape\Desktop\New folder (6)\AS\JLUP_104068\tx1.xml'
#file_jss=r'C:\Users\digiscape\Desktop\New folder (6)\AS\JLUP_104068\JLUP-jss.xml'
#print(BRX010_42(file_jss,file_xml))
