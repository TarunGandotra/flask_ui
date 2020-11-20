from bs4 import BeautifulSoup
import os
import re
import logging
def multifind(string, value, start = 0, stop = None):
    values = []
    while True:
        found = string.find(value, start, stop)
        if found == -1:
            break
        values.append(found)
        start = found + 1
    return values

def BRX005A(appfile, style):
    try:
        list1=[]
        list2=[]
        final_list=[]
        #style="C:/Users/digiscape/Desktop/JOURNAL"

        file=open(style,encoding="utf-8")
        soup=BeautifulSoup(file,'xml')

        string=""
        for j in soup.find_all('refStyle'):
            string=j.get_text()
            #print(j)
        if(string==""):
            return [["BRX005A","Bibliographic reference cross-references","the text cross-references take the form of a superscript Arabic number (or, for multiple citations, superscript numbers separated by a comma","no error"]]
        if(string[0].isdigit() and ((string[0]=='3' and string[1]=='a')or string[0]=='6' or (string[0]=='9' and string[1]=='a'))):
            l=[]
            l1=[]
            l11=[]
            E1=0;E2=0
            file1=open(appfile,encoding="utf-8")
            #print(file1)
            soup=BeautifulSoup(file1,'xml')
            #print(soup)
            soup1=str(soup)
            lf= multifind(soup1,'<cross-ref')
            
            for k in lf:
                #print(re.split())
                #print(soup1[k+31:k+34]=="bib")
                if (soup1[k+31:k+34]=="bib"):
                    l=re.findall('<sup>.*?</sup>',soup1[k:k+66])
                    #print(l)
                    if l==[]:
                        #E1=1
                        list1=["BRX005A","Bibliographic reference cross-references","the text cross-references take the form of a superscript Arabic number (or, for multiple citations, superscript numbers separated by a comma","error",str(k),"superscript not present"]
                        final_list.append(list1)
                    else:
                        if (l[0][5:-6]).isdigit()==False:
                            #E2=1
                            list1=["BRX005A","Bibliographic reference cross-references","the text cross-references take the form of a superscript Arabic number (or, for multiple citations, superscript numbers separated by a comma","error",str(k),"superscript not Arabic number"]
                            final_list.append(list1)
            for j in lf:
                #print(j)
                #print(soup1[j+33:j+36])
                if(soup1[j+33:j+36]=="bib"):
                    #print(soup1[j:j+60])
                    l1=re.findall('<sup>.*?</sup>',str(k))
                    #print(l1)
                    if l1==[]:
                        #E1=1
                        list1=["BRX005A","Bibliographic reference cross-references","the text cross-references take the form of a superscript Arabic number (or, for multiple citations, superscript numbers separated by a comma","error",str(j),"superscript not present"]
                        final_list.append(list1)
        else:
            return [["BRX005A","Bibliographic reference cross-references","the text cross-references take the form of a superscript Arabic number (or, for multiple citations, superscript numbers separated by a comma","no error"]]
        if final_list==[]:
            return [["BRX005A","Bibliographic reference cross-references","the text cross-references take the form of a superscript Arabic number (or, for multiple citations, superscript numbers separated by a comma","no error"]]
        return final_list
    except Exception as e:
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX005A Bibliographic reference cross-references " )
        logging.shutdown()
        return [["BRX005A","Bibliographic reference cross-references","the text cross-references take the form of a superscript Arabic number (or, for multiple citations, superscript numbers separated by a comma","no error"]]
    
#print(BRX005A("C:/Users/digiscape/Desktop/folder2/APME-jss.xml","C:/Users/digiscape/Desktop/rulexml/CANEP_1534.xml"))
# file_jss =r'C:/Users/Digiscape/Desktop/sindhu/COLEGN_607----Rule no. BRF020A, BRF027, BRF028, BRF034, BRF037A, BRF032A/COLEGN-jss.xml'
# file_xml =r'C:/Users/Digiscape/Desktop/sindhu/COLEGN_607----Rule no. BRF020A, BRF027, BRF028, BRF034, BRF037A, BRF032A/tx1.xml'
# print(BRX005A(file_xml,file_jss))

#file_jss = 'C:/Users/Digiscape/Desktop/sindhu/test_folder/APME-jss.xml'
#file_xml = 'C:/Users/Digiscape/Desktop/sindhu/test_folder/CANEP_1534.xml'
#print(BRX005A(file_xml,file_jss))
