from bs4 import BeautifulSoup
import logging

def label(file):

    count = 0
    h=[]
    error = []
    try:
        with open(file,'r',encoding= "utf-8") as f:
            contents = f.read()
            soup = BeautifulSoup(contents,"lxml")
            for i in soup.find_all("ce:label"):
                #print(i.text)
                h.append(i.text)
        #print(h)
        for i in h:
            #str1=str(i)
            if i.endswith('.') or i.endswith(',') or i.endswith(':'):
                error.append(['XsBM2.01','Body matter','Check absence end punctuation in labels','error',str(contents.index(i)),'ce:label ends with special characters.'])
            else:
                pass
        if error == []:
            rule_file=[]
            rule_file.append('XsBM2.01')
            rule_file.append("Body matter")
            rule_file.append('Check absence end punctuation in labels')
            rule_file.append("no error")
            error.append(rule_file)
    except Exception as e:
        print('HERE', e)
        rule_file=[]
        rule_file.append('XsBM2.01')
        rule_file.append("Body matter")
        rule_file.append('Check absence end punctuation in labels')
        rule_file.append("no error")
        error.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in XsBM2.01 : Body matter " )
        logging.shutdown()


    return error


#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\tx1.xml'
#print(label(file))
