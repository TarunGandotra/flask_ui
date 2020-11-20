
import re
import sys
from bs4 import BeautifulSoup
import logging

def Brx042(path):
    
    List=[]
    try:
        coun=0
        infile = open(path,"r",encoding="utf-8")
        soup=BeautifulSoup(infile,'lxml')
        soup1 = str(soup)
        abstract=soup.find_all('ce:abstract')
        text=[item.get_text() for item in abstract]
        if(len(text)>0):
            textw=""
            for what in text:
                if(what!="\n"):
                    textw=textw+what

            reference=soup.find_all('ce:bibliography')

            text1=[item.get_text() for item in reference]
            if(len(text1)>0):
                text1w=""
                for what1 in text1:
                    text1w=text1w+what1
                ref1=text1w.split('[')
                main_text=soup.find_all('ce:sections')

                text2=[item.get_text() for item in main_text]
                if len(text2)>0:
                    string2=""
                    for what2 in text2:
                        string2=string2+what2

                    ref=[]
                    for ind,item in enumerate(ref1):
                        if(item[:-1]!="Reference"):
                            if(']' in item):
                                ref.append(item[item.index(']')+1:])

                    dictio={5:"replace the citation with name date cross ref",2:"ERROR:name-date crossref not in appropriate style",4:"ERROR:REFERENCE not added to bibliography",3:"ËRROR: reference cited full in abstract"}
                    for ind in range(len((textw))):
                        coun=0
                        s=""
                        if textw[ind]=='[':
                            for i in range(ind+1,len(textw)):
                                if(textw[i]==']'):
                                    break
                                else:
                                    s=s+textw[i]

                            lis1=re.findall('[a-zA-z]+\s',s)
                            lis2=re.findall("\(\d\d\d\d\)",s)
                            if(len(lis1)>0 and len(lis2)>0):
                                if s in string2:
                                    s1=""
                                    for item2 in lis1:
                                        s1=s1+item2
                                    s2=""
                                    for item3 in lis2:
                                        s2=s2+item
                                    if(len(s)<5000):
                                        indlis=soup1.index(s)
                                        coun=4
                                        if s in ref_lis:
                                            coun=3
                                        else:
                                            for item4 in ref_lis:
                                                if s1 in item4 and s2 in item4:
                                                    coun=2;
                                                    if(s1+s2==s):
                                                        coun=1
                                                    break
                            else:

                                lis5=re.findall("\d+",s)#check whether the braces contains numbers or not
                                if(len(lis5)>0):
                                    ser='['+s+']' 
                                    if ser in string2:

                                        indlis=soup1.index(lis5[0])
                                        lis7=re.findall('[a-zA-Z]+\s\(\d\d\d\d\)\s\[\d+',textw[:i+2])
                                        #then look for all the occurences of Name (year) [Number
                                        if(len(lis7)>0):
                                        #if such occurences exist,then take the last one appearing in the list as that is the one which contain the occurence corresponding to that index 
                                            l7=lis7[-1]
                                            s7=l7[-1]
                                            s3=""
                                            for char in s7:    #take all the chars before the opening sq. brace
                                                if(s7.index(char)<s7.index('[')):
                                                    s3=s3+char
                                                    break
                                            for refs in ref: #check whether the occurence exist in one of the references in the reference list
                                                if s3 in refs:
                                                    coun=1    # if yes coun==1
                                                    break
                                            if(coun!=1):
                                                coun=4    # else coun==4
                                        else:

                                            coun=5;





                        if(coun!=0 and coun!=1):
                            List.append(["BRX042","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and that is also cited in the main body of the text replace the citation","error",str(indlis),dictio[coun]])
                            coun=0
        if(len(List)==0):

            List.append(["BRX042","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and that is also cited in the main body of the text replace the citation","no error"])
        return List
    
    except Exception as e:
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX042 : Bibliographic reference cross-references " )
        logging.shutdown()

        lst1=["BRX042","Bibliographic reference cross-references","For a numbered reference cited in full in the abstract and that is also cited in the main body of the text replace the citation","no error"]
        List.append(lst1)
        return List
        
#file_xml =r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(Brx042(file_xml))
