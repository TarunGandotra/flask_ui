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

def BRX007(appfile,style):

    #style="C:/Users/digiscape/Desktop/folder"
    try:
        list1=[]
        list2=[]
        final_list=[]
        styl=[]
        file=open(style,"r",encoding="utf-8")
        soup=BeautifulSoup(file,'xml')

        string=""
        for j in soup.find_all('refStyle'):
            string=j.get_text()
            #print(j)
        if(string==""):
            return ["BRX007","Bibliographic reference cross-references""aid","no error"]
        if(string[0].isdigit() and ((string[0]=='3' and string[1]=='a')or string[0]=='6' or (string[0]=='9' and string[1]=='a'))):
            filea=open(appfile,encoding='utf-8')
            #print(filea)
            soup=BeautifulSoup(filea,'xml')
            #print(soup)
            soup=str(soup)
            #print(soup)
            l = multifind(soup,'<cross-ref')
            #print(l)
            for i in l:
                i1=(soup[i+40:i+61])
                #print(i1)
                if(re.findall('<sup>.*?</sup>',i1)!=[]):
                    if(soup[i+46]==" "):
                        list1=["BRX007","Bibliographic reference cross-references","the superscript reference citations (cross-references) are closed up to the preceding text","error",str(i+45),"Superscript not closed up to the preceding text"]
                        final_list.append(list1)
                    if(soup[i-1]==">"):
                        i12=i-1
                        while(soup[i12]!="<"):
                            i12=i12-1
                        if(soup[i12-1]==":" or soup[i12-1]==";"):
                            list1=["BRX007","Bibliographic reference cross-references","the superscript reference citations (cross-references) are closed up to the preceding text","error",str(i12-1),"Superscript after colon or semicolon"]
                            fianl_list.append(list1)
                    elif(soup[i-1]==":" or soup[i-1]==";"):
                        list1=["BRX007","Bibliographic reference cross-references","the superscript reference citations (cross-references) are closed up to the preceding text","error",str(i-1),"Superscript after colon or semicolon"]
                        final_list.append(list1)
                    i13=i
                    while(soup[i13]!="/"):
                        i13=i13+1
                    if(soup[i13+17]=="." or soup[i13+17]==","):
                        list1=["BRX007","Bibliographic reference cross-references","the superscript reference citations (cross-references) are closed up to the preceding text","error",str(i13+17),"Superscript before full stop or comma"]
                        final_list.append(list1)
        if final_list==[]:
            return ([["BRX007","Bibliographic reference cross-references","the superscript reference citations (cross-references) are closed up to the preceding text","no error"]])
        return final_list
    except Exception as e:
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX007 : Bibliographic reference cross-references " )
        logging.shutdown()
        return ([["BRX007","Bibliographic reference cross-references","the superscript reference citations (cross-references) are closed up to the preceding text","no error"]])
#print(BRX007("C:/Users/digiscape/Desktop/rulexml/CANEP_1534.xml","C:/Users/digiscape/Desktop/folder2/APME-jss.xml"))
