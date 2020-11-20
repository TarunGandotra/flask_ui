import re
from bs4 import BeautifulSoup
import logging

def BRX005B_36(file_xml,file_jss):
    rule_err = []
    error = []
    listj =['6 AMA','3a Embellished Vancouver']
    list1=[]
    try:
        with open(file_jss,'r',encoding ='utf-8') as f1:
            contents1=f1.read()
            soup1=BeautifulSoup(contents1,'lxml')
            for ref in soup1.find_all('refstyle'):
                refr=ref.text
                if refr in listj:
                    with open(file_xml,'r',encoding ='utf-8') as f:
                        contents = f.read()
                        soup = BeautifulSoup(contents,'lxml')
                        list_tag=['book-review','article','simple-article']
                        count = 0
                        for sec in soup.find_all('ce:sections'):
                            for para in sec.find_all('ce:para'):
                                cross_ref=['ce:cross-refs']
                                for tag in para.find_all(cross_ref):
                                    #print(tag.attrs['refid'],'???'*20)
                                    k=tag.attrs['refid']
                                    n= re.findall(r"^bib",k)
                                    if bool(n)==True:
                                        #print(k,'$$'*50)
                                        if 'ce:sup'in str(tag):
                                            for sup in tag.find_all('ce:sup'):
                                                #print(sup,tag.attrs['id'],'founddd')
                                                str1=(sup.text)
                                                str2=str1.split(',')
                                                #print(str2)
                                                if (len(str2))==1:
                                                    #print(k)
                                                    #print('only one element')
                                                    pass
                                                else:
                                                    for i in range(1,len(str2)): 
                                                        if str2[i].startswith(' '):
                                                            #print('error')
                                                            error.append([str(contents.index(str(tag.attrs['id']))),"in multiple citations of this type(superscripted) there have (keyboard) space after the comma[Error]."])
                                                        else:
                                                            #print('No error',str2[i],contents.index(str(tag.attrs['id'])))
                                                            error.append([str(contents.index(str(tag.attrs['id']))),"in multiple citations of this type there have no (keyboard) space after the comma."])
                                            #pass
                                                #print(sup)
                                        else:
                                            index=contents.index(tag.attrs['id'])
                                            #index=[str(contents.index(str(tag.attrs['id'])))]
                                            #print(index,'indexxxxxxxxx')
                                            w=index
                                            #print(type(w))
                                            #w=(int(index[0]))
                                            #print(w)
                                            stri=(contents[w-100:w])
                                            #print(stri,'333333333333333333333333')
                                            #print('--'*60)
                                            #ref_lst=['References','Ref.','Ref','Refs','Reference']
                                            if "Ref." in stri or "Refs." in stri or "Reference" in stri or "References" in stri:
                                                str1=(tag.text)
                                                str2=str1.split(',')
                                                #print(str2)
                                                if (len(str2))==1:
                                                    print(k)
                                                    print('only one element')
                                                    #pass
                                                else:
                                                    for i in range(1,len(str2)): 
                                                        if str2[i].startswith(' '):
                                                            pass
                                                            #print('no error')
                                                        else:
                                                            #print('error',str2[i],contents.index(str(tag.attrs['id'])))
                                                            error.append([str(contents.index(str(tag.attrs['id']))),"in multiple citations of this type there have no (keyboard) space after the comma."])
                                                
                                            else:
                                                #print('errorrrr')
                                                error.append([str(contents.index(str(tag.attrs['id']))),"Uncited references but the cross-reference number(s) is on the line"])
                                    else:
                                        pass
                else:
                    pass
        
        if error!=[]:
            for i in error:
                rule_file=[]
                rule_file.append("BRX005B(36-37)")
                rule_file.append('Bibliographic reference cross-references')
                rule_file.append("If Reference cited, in which case the cross-reference number(s) should be on the line.")
                rule_file.append("error")
                rule_file.append(i[0])
                rule_file.append(i[1])
                rule_err.append(rule_file)
        else:
            rule_file=[]
            rule_file.append("BRX005B(36-37)")
            rule_file.append("Bibliographic reference cross-references")
            rule_file.append('in multiple citations of this type there should be a (keyboard) space after the comma.')
            rule_file.append("no error")
            rule_err.append(rule_file)
    except Exception as e:
        print(e)
        rule_file=[]
        rule_file.append("BRX005B(36-37)")
        rule_file.append("Bibliographic reference cross-references")
        rule_file.append('in multiple citations of this type there should be a (keyboard) space after the comma.')
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX005B(36-37) : Bibliographic reference cross-references " )
        logging.shutdown()
                    

    return rule_err 
#file_xml=r'C:\Users\digiscape\Desktop\Error_file\YCTIM_102195\tx1.xml'
#file_jss=r'C:\Users\digiscape\Desktop\Error_file\YCTIM_102195\YCTIM-jss.xml'
#print(BRX005B_36(file_xml,file_jss))
