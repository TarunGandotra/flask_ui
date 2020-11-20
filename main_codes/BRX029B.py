#THE_CODE_ARENA
import os
import re
from bs4 import BeautifulSoup
import logging


def brx029b(path,pathjss):
    try:
        injss=open(pathjss,'r',encoding="utf8")
        soup2=BeautifulSoup(injss,'xml')
        refsty=soup2.find_all('refStyle')
        for ite in refsty:
            if ite.get_text()=="":
                return [["BRX029B..","Bibliographic reference cross-references","[APA] Use 'a’and 'b' after the year only if all authors’ names as well as the year are identical","no error"]]
            elif ite.get_text()=="5 APA":
                count9=0
                filelist1=[]
                infile = open(path,"r",encoding="utf8")
                content=infile.read()
                soup1=BeautifulSoup(content,'lxml')
                soup3=str(soup1)
                List=[]
                dates=[]
                labels=[]
                for tags in soup1.find_all("ce:bib-reference"):
                    l=[]
                    g=[]
                    L=[]
                    for o in tags.find_all("ce:label"):
                        z=o.text
                        labels.append(z)
                    for i in tags.find_all("ce:given-name"):
                        l.append(i.text)
                    for j in tags.find_all("ce:surname"):
                        g.append(j.text)

                    if(len(l)>0):
                        for index1 in range(len(l)):
                            s=l[index1]+g[index1]
                            L.append(s)
                    else:
                        if(len(g)>0):
                            for index1 in range(len(g)):
                                s=g[index1]
                                L.append(s)
                    #print('the list in l-----',l)
                    #print('the list in L-------',L)
                    for ij in tags.find_all("sb:date"):
                        if (len(l)>0 or len(g)>0):
                            dates.append(ij.text)
                            count9=1
                    if len(dates)>0 and count9==1:
                        L.append(dates[-1])
                        count9=0


                    List.append(L)
            #print(len(List))
            #print(List)
            else:
                return [["BRX029B..","Bibliographic reference cross-references","[APA] Use 'a’and 'b' after the year only if all authors’ names as well as the year are identical","no error"]]

            List2=[]
            for index1,item1 in enumerate(List):
                #print(List)
                for index2 in range(len(List)):
                    if item1==List[index2] and index1!=index2:
                        List2.append((index1,item1))
            Dup_Label=[]
            for a,b in List2:
                if(len(b)>0):
                    Dup_Label.append(labels[a])
            for lab in Dup_Label:
                #print(lab)
                if lab[-1].isdigit():
                    indices1=soup3.index(lab)
                    #print('error0')
                    filelist1.append(["BRX029B","Bibliographic reference cross-references","[APA] Use 'a’and 'b' after the year only if all authors’ names as well as the year are identical",'error',str(indices1),"Error:should have latin letters at end if all author's name and year are equal"])
                else:
                    soup_crossref=BeautifulSoup(content,'lxml')
                    cross_ref=soup_crossref.find_all('ce:cross-ref')
                    crosslist=[]
                    crossref=[]
                    for tags in cross_ref:
                        if tags['refid'][:3]=='bib':
                            crosslist.append(tags)
                    for item in crosslist:
                        crossref.append(item.text)
                    for item5 in Dup_Label:
                        if item5[:-1] in crossref:
                            indices1=soup3.index(item5)
                            #print('error1')
                            filelist1.append(["BRX029B","jid","[APA] Use 'a’and 'b' after the year only if all authors’ names as well as the year are identical",'error',str(indices1),"Error:citation should use a and b as corresponding reference has all authors name and year identical to other referene also"])
        if len(filelist1)==0:
            filelist1.append(["BRX029B","Bibliographic reference cross-references","[APA] Use 'a’and 'b' after the year only if all authors’ names as well as the year are identical","no error"])
            return filelist1


        else:
            return [["BRX029B","Bibliographic reference cross-references","[APA] Use 'a’and 'b' after the year only if all authors’ names as well as the year are identical","no error"]]
    except Exception as e:
        print(e)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX029B : Bibliographic reference cross-references " )
        logging.shutdown()
        List25=[]
        List25.append(["BRX029B","Bibliographic reference cross-references","[APA] Use 'a’and 'b' after the year only if all authors’ names as well as the year are identical","no error"])
        return List25
    

# jsspath =r'C:\Users\digiscape\Desktop\file_log\DRUPOL_2511/DRUPOL-jss.xml'
# filepath =r'C:\Users\digiscape\Desktop\file_log\DRUPOL_2511/tx1.xml'
# print(brx029b(filepath,jsspath))
