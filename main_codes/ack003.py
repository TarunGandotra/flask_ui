from bs4 import BeautifulSoup
import re
def fack003(file):
    for_demo2 = [] 
    count = 0
    with open(file,'r',encoding ='utf-8') as f:
        contents=f.read()
        soup = BeautifulSoup(contents,"lxml")
        count=0
        for i in soup.find_all('ce:acknowledgment'):
            count+=1
            #print(count,i.name)
        if count != 1:

            #print('error')
            for_demo2.append("ack003")
            for_demo2.append("acknowledgment")
            for_demo2.append("jid")
            for_demo2.append("index")
            for_demo2.append("error")
            for_demo2.append("acknowledgment tag comes more than one time")

        else:
            for_demo2.append("ack003")
            for_demo2.append("aid")
            for_demo2.append("jid")
            for_demo2.append("no error")


    return for_demo2
        #print('pass')
#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATB_17604_110\fs.xml'
#print(fack003(file))
