import re
from bs4 import BeautifulSoup
import logging

def BRX005B_35(file_xml,file_jss):
    rule_err = []
    error = []
    listj =[]
    refs_list1=['6 AMA','3a Embellished Vancouver']
    try:
        with open(file_jss,'r',encoding ='utf-8') as f1:
            content1=f1.read()
            soup1=BeautifulSoup(content1,'lxml')
            for refs in soup1.find_all('refstyle'):
                refst=(refs.text)
            #print(refst,'123456789987')
            if refst in refs_list1:
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
                                #print(k,'$$'*50)
                                if 'ce:sup'in str(tag):
                                    for sup in tag.find_all('ce:sup'):
                                    #print(sup,tag.attrs['id'],contents.index(tag.attrs['id']),'founddddddddddddddddd')
                                        loc=(contents.index(tag.attrs['id']))
                                        str2=(contents[loc-50:loc])
                                        #print(str2)
                                        if "Ref." in str2 or "Refs." in str2 or "Reference" in str2 or "References" in str2 :
                                            if ' Citation."/>' in str2:
                                                pass
                                            else:
                                                error.append([str(contents.index(tag.attrs['id'])),"Text References cited but the cross-reference number(s) is also Superscipted[Error]"])
                                                #print('reference found means error')
                                        
                                        else:
                                        
                                            pass
                                        #print('-'*80)
                                        #print(sup)
                                else:
                                    #print('not found',tag,[str(contents.index(str(tag)))])
                                    index=[str(contents.index(str(tag)))]
                                    w=(int(index[0]))
                                    stri=(contents[w-100:w])
                                    #print(stri,'333333333333333333333333')
                                    #print('--'*60)
                                    if "Ref." in stri or "Refs." in stri or "Reference" in stri or "References" in stri:
                                        #print('reference found means no error')
                                        pass
                                    else:
                                        #print('error')
                                        error.append([str(contents.index(str(tag))),"Uncited references but the cross-reference number(s) is on the line"])
                            else:
                                pass
            if error!=[]:
                for i in error:
                    rule_file=[]
                    rule_file.append("BRX005B--35")
                    rule_file.append('Bibliographic reference cross-references')
                    rule_file.append("If Reference cited, in this case the cross-reference number(s) should be on the line & vice-versa.")
                    rule_file.append("error")
                    rule_file.append(i[0])
                    rule_file.append(i[1])
                    rule_err.append(rule_file)
            else:
                rule_file=[]
                rule_file.append("BRX005B--35")
                rule_file.append("Bibliographic reference cross-references")
                rule_file.append('If Reference cited, in this case the cross-reference number(s) should be on the line & vice-versa.')
                rule_file.append("no error")
                rule_err.append(rule_file)
    except Exception as e:
        print(e)
        rule_file=[]
        rule_file.append("BRX005B--35")
        rule_file.append("Bibliographic reference cross-references")
        rule_file.append('If Reference cited, in this case the cross-reference number(s) should be on the line & vice-versa')
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX005B--35 : Bibliographic reference cross-references " )
        logging.shutdown()
                    

    return rule_err 
#file_xml=r'C:\Users\digiscape\Desktop\Error_file\YCTIM_102195\tx1.xml'
#file_jss=r'C:\Users\digiscape\Desktop\Error_file\YCTIM_102195\YCTIM-jss.xml'
#print(BRX005B_35(file_xml,file_jss))
