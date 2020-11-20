from bs4 import BeautifulSoup
import logging
def keywords(file):
    error= []
    try:
        count = 0
        h=[]
        
        with open(file,'r',encoding= "utf-8") as f:
            contents = f.read()
            soup = BeautifulSoup(contents,"lxml")
            for i in soup.find_all("ce:keywords"):
                #print(i.text)
                for j in i.find_all('ce:text'):
                    #print(j.text)
                    h.append(j.text)
        #print(h)
        for i in h:
            #str1=str(i)
            if i.endswith('.') or i.endswith(',') or i.endswith(':'):
                error.append(['XsFM1.09','Front matter','Check for the punctuation of keywords','error',str(contents.index(i)),'ce:keywords ends with special characters.'])
            else:
                pass
        if error == []:
            rule_file=[]
            rule_file.append('XsFM1.09')
            rule_file.append("Front matter")
            rule_file.append('Check for the punctuation of keywords')
            rule_file.append("no error")
            error.append(rule_file)
    except Exception as e:
        #print('HERE', e)
        rule_file=[]
        rule_file.append('XsFM1.09')
        rule_file.append("Front matter")
        rule_file.append('Check for the punctuation of keywords')
        rule_file.append("no error")
        error.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in XsFM1.09 : Front matter " )
        logging.shutdown()
    return error

#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\tx1.xml'
#print(keywords(file))
