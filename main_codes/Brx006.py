from bs4 import BeautifulSoup
import re
import logging
def BRX006(file_xml, file_jss):
    rule_err = []
    error = []
    listj =[]
    refs_list1=['1 Numbered']
    try:
        with open(file_jss,'r',encoding ='utf-8') as f1:
            content1=f1.read()
            soup1=BeautifulSoup(content1,'lxml')
            for refs in soup1.find_all('refstyle'):
                refst=(refs.text)
            if refst in refs_list1:
                with open(file_xml,'r',encoding ='utf-8') as f:
                    contents = f.read()
                #print(contents[23735:23745])
                soup = BeautifulSoup(contents,'lxml')
                count = 0
                lst=['. [',': [','; [',', [']
                lst2_ref=['ref. ','refs. ','Ref. ','Refs. ']
                for sec in soup.find_all('ce:sections'):
                    for para in sec.find_all('ce:para'):
                        cross_ref=['ce:cross-ref','ce:cross-refs']
                        for tag in para.find_all(cross_ref):
                            #print(tag.attrs['refid'],'???'*20)
                            k=tag.attrs['refid']
                            n= re.findall(r"^bib",k)
                            if bool(n)==True:
                                count+=1
                                loca=contents.index(tag.attrs['id'])
                                str_loca=contents[loca-50:loca]
                                #print(count,' : ',str_loca)
                                if [ele1 for ele1 in lst if(ele1 in str_loca)]:
                                    #print('error found',para.attrs['id'],str_loca,loca-20)
                                    if [ele1 for ele1 in lst2_ref if(ele1 in str_loca)]:
                                        #print('no error')
                                        pass
                                    else:
                                        #print('error confirm')
                                        #print(type(str(loca-20)))
                                        error.append([str(loca-20),'text citations should be placed before relevant punctuation in all cases but here error' ])
                               
                            else:
                                pass
            if error!=[]:
                for i in error:
                    rule_file=[]
                    rule_file.append("BRX006")
                    rule_file.append('Bibliographic reference cross-references')
                    rule_file.append("text citations should be placed before relevant punctuation in all cases")
                    rule_file.append("error")
                    rule_file.append(i[0])
                    rule_file.append(i[1])
                    rule_err.append(rule_file)
            else:
                rule_file=[]
                rule_file.append("BRX006")
                rule_file.append("Bibliographic reference cross-references")
                rule_file.append('text citations should be placed before relevant punctuation in all cases')
                rule_file.append("no error")
                rule_err.append(rule_file)
    except Exception as e:
        print(e)
        rule_file=[]
        rule_file.append("BRX006")
        rule_file.append("Bibliographic reference cross-references")
        rule_file.append('text citations should be placed before relevant punctuation in all cases')
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX005B(36-37) : Bibliographic reference cross-references " )
        logging.shutdown()
                    

    return rule_err 
# file_xml=r'C:\Users\digiscape\Desktop\APCATB_118473\tx1.xml'
# file_jss=r'C:\Users\digiscape\Desktop\APCATB_118473\APCATB-jss.xml'
# print(BRX006(file_xml,file_jss))
