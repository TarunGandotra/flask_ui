import os
import re
from bs4 import BeautifulSoup
import logging

def brx030(pathxml,pathjss):
    try:
        injss=open(pathjss,'r',encoding="utf8")
        soup2=BeautifulSoup(injss,'xml')
        refsty=soup2.find_all('refStyle')
        for ite in refsty:
            if ite.get_text()=="":
                return [["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","no error"]]
            elif ite.get_text()=="5 APA":
                Lst=[]
                list2=[]
                infile=open(pathxml,'r',encoding='utf-8')
                soup=BeautifulSoup(infile,'lxml')
                soup3=str(soup)
                list1=soup.find_all('ce:cross-ref')

                for tags in list1:
                    if tags['refid'][:3]=='bib':
                        list2.append(tags.text)
                list3=[]
                for item1 in list2:
                    if 'et al.' in item1:
                        list3.append(item1)
                list4=[]
                for item2 in list2:
                    if ' and ' in item2:
                        list4.append(item2)


                list5=[]
                for item3 in list2:
                    if ' & ' in item3:
                        list5.append(item3)


                for item4 in list3:
                    if(len(list3)>0):
                        n=item4.index('et al.')
                        item5=item4[:n]
                        if item5[-2]==',' or item5[-1]==",":

                            list6=re.findall('\,',item5[:-2])
                            if len(list6)>=1:
                                continue
                            else:
                                indices=soup3.index(item5)
                                Lst.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","error",str(indices),"Error:only one name preceds,therefore no comma before et al."])         
                        else:
                            list6=re.findall('\,',item5[:-2])
                            if len(list6)>=1:
                                indices=soup3.index(item5)
                                Lst.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","error,",str(indices),"Error:more than one name preceds,therefore comma before et al."])
                            else:
                                continue



                for item6 in list4:
                    if(len(list4)>0):
                        n=item6.index(' and')
                        item7=item6[:n]
                        if item7[-1]==',' or item7[-2]==",":
                            
                            list7=re.findall('\,',item7[:-1])
                            if len(list7)>=1:
                                continue
                            else:
                                voila=0;
                                itrolist=[]
                                itrolist.append(0)
                                for indexo in range(len(item7[:-1])):
                                    if item7[indexo]==",":
                                        itrolist.append(indexo)
                                itrolist.append(len(item7[:-1]))
                                for commaindex in range(1,len(itrolist)):
                                    if abs(itrolist[commaindex]-itrolist[commaindex-1])>35:
                                        voila=1;
                                        break;
                                if voila==1:
                                    continue
                                else:
                                    indices=soup3.index(item7)
                                    Lst.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","error",str(indices),"Error:only one name preceds,therefore no comma before and"])

                        else:
                            list7=re.findall('\,',item7[:-1])
                            if len(list7)>=1:
                                voila=0;
                                itrolist=[]
                                itrolist.append(0)
                                for indexo in range(len(item7[:-1])):
                                    if item7[indexo]==",":
                                        itrolist.append(indexo)
                                itrolist.append(len(item7[:-1]))
                                for commaindex in range(1,len(itrolist)):
                                    if abs(itrolist[commaindex]-itrolist[commaindex-1])>=35:
                                        voila=1;
                                        break;
                                if voila==1:
                                    continue
                                else:
                                    indices=soup3.index(item7)
                                    Lst.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","error",str(indices),"more than one name preceds,therefore comma before and"])
                            else:
                                continue


                for item8 in list5:

                    if(len(list5)>0):
                        n=item8.index("&")
                        item9=item8[:n]
                        if item9[-1]==',' or item9[-2]==',':
                            list8=re.findall('\,',item9[:-1])
                            if len(list8)>=1:
                                continue
                            else:
                                voila=0;
                                itrolist=[]
                                itrolist.append(0)
                                for indexo in range(len(item9[:-1])):
                                    if item9[indexo]==",":
                                        itrolist.append(indexo)
                                itrolist.append(len(item9[:-1]))
                                for commaindex in range(1,len(itrolist)):
                                    if abs(itrolist[commaindex]-itrolist[commaindex-1])>35:
                                        voila=1;
                                        break;
                                if voila==1:
                                    continue
                                else:
                                    indices=soup3.index(item9)
                                    Lst.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","error",str(indices),"Error:only one name preceds,therefore no comma before &"])

                        else:
                            list8=re.findall('\,',item9[:-1])
                            if len(list8)>=1:

                                voila=0;
                                itrolist=[]
                                itrolist.append(0)
                                for indexo in range(len(item9[:-1])):
                                    if item9[indexo]==",":
                                        itrolist.append(indexo)
                                itrolist.append(len(item9[:-1]))

                                for commaindex in range(1,len(itrolist)):

                                    if itrolist[commaindex]-itrolist[commaindex-1]>35:
                                        voila=1;
                                        break;
                                if voila==1:
                                    continue
                                else:
                                    indices=soup3.index(item9)
                                    Lst.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","error",str(indices),"Error:more than one name preceds therefore comma before &"])
                            else:
                                continue
                if len(Lst)==0:
                    Lst.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","no error"])
                return Lst
            else:
                return [["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","no error"]]
    except Exception as e:
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX030 : Bibliographic reference cross-references " )
        logging.shutdown()
        List25=[]
        List25.append(["BRX030","Bibliographic reference cross-references","[APA] Note: from the examples it can be seen that, if just one name precedes it","no error"])
        return List25
#file_jss =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/APCATA-jss.xml'
#file_xml =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(brx030(file_xml,file_jss))
