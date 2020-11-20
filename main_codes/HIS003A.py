from bs4 import BeautifulSoup
import re
import logging

def rule_HIS003A(file_xml,file_jss):
#count = 0
#lst1=[]
    err_rule=[]
    error=[]
    jss_tags=[]

    try:
        with open (file_jss,'r',encoding ='utf-8') as f:
            contents = f.read()
            soup = BeautifulSoup(contents,"lxml")
            for i in soup.find_all('history'):
                #jss_tags.append((i.text))
                for k in i.find_all('journalspecifichistorycomment'):
                    #print(k.text)
                    jss_tags.append((k.text))
            #print(jss_tags)
        lst2=[]
        with open(file_xml,'r',encoding ='utf-8') as f1:
            contents = f1.read()
            soup = BeautifulSoup(contents,"lxml")
            for i in soup.find_all('ce:miscellaneous'):
                lst2.append(i.text)
                lst2_join = ''.join(lst2)
                #print(lst2_join)
            for i in jss_tags:
                if i=='3':
                    if (lst2_join.find('Communicated by') == 3):
                        error.append([str(contents.index('Communicated by')),"Communicated by is missing in ce:miscellaneous tag"])
            if error!=[]:
                for i in error:
                    rule_file=[]
                    rule_file.append("HIS003A")
                    rule_file.append('Article history')
                    rule_file.append("The most common information captured using this element is the communicating editor")
                    rule_file.append("error")
                    rule_file.append(i[0])
                    rule_file.append(i[1])
                    err_rule.append(rule_file)
                pass
                #print('error')
            else:
                rule_file=[]
                rule_file.append("HIS003A")
                rule_file.append("Article-History")
                rule_file.append('The most common information captured using this element is the communicating editor')
                rule_file.append("no error")
                err_rule.append(rule_file)
    except:
        rule_file=[]
        rule_file.append("HIS003A")
        rule_file.append("Article-History")
        rule_file.append('The most common information captured using this element is the communicating editor')
        rule_file.append("no error")
        err_rule.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in HIS003A : Article-History " )
        logging.shutdown()

    return err_rule

#file_jss =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/APCATA-jss.xml'
#file_xml =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(rule_HIS003A(file_xml,file_jss))
                #print('no error')
