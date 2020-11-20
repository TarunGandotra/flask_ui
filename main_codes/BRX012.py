from bs4 import BeautifulSoup
import re

def Brx012(file):
    for_demo2 = []
    biblio = []
    bibreglst = []
    crossref = []
    crossreflst = []
    count = 0
    
    with open(file,'r',encoding = 'utf-8') as f:
        contents = f.read()
        #print(contents[60])
        soup = BeautifulSoup(contents, 'lxml')
        for bib in soup.find_all('ce:bibliography'):
            for bibref in bib.find_all('ce:bib-reference'):
                for label in bibref.find_all('ce:label'):
                    biblio.append(label.text)


        for i in soup.find_all('ce:cross-ref'):
            crossref.append(i.text)

        for values in biblio:
            bibreg = re.sub('[^a-zA-Z0-9]+','', values)
            bibreglst.append(bibreg)
        #print(bibreglst)


        for values in crossref:
            crossrefreg = re.sub('[^a-zA-Z0-9]+','', values)
            crossreflst.append(crossrefreg)
        #print(crossreflst)


        for values in bibreglst:
            if values not in crossreflst:
                count += 1
                for_demo2.append(['BRX012','AID','JID','error',str(contents.index(values[0])),'Bibliography and Cross Reference are not matching'])  
            else:
                continue

        if count == 0:
            for_demo2.append('BRX012')  
            for_demo2.append('AID')
            for_demo2.append('JID')
            for_demo2.append('no error')
        return for_demo2
#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(Brx012(file))