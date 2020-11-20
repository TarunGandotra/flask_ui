#rule(ack003)
from bs4 import BeautifulSoup
import re
import logging

def ack003(file):
    #for_demo2 = [] 
    err_rule=[]
    error=[]
    count = 0
    try:
        with open(file,'r',encoding ='utf-8') as f:
            contents=f.read()
            soup = BeautifulSoup(contents,"lxml")
            count=0
            for i in soup.find_all('ce:acknowledgment'):
                count+=1
                #print(count,i.name)
            if count!=0:
                if count != 1:
                    error.append([str(contents.index('ce:acknowledgment')),"acknowledgment tag comes more than one time"])
                if error!=[]:
                    for i in error:

                        #print('error')
                        for_demo2=[]
                        for_demo2.append("ack003")
                        for_demo2.append("Acknowledgements")
                        for_demo2.append("The DTD allows multiple ce:acknowledgements to be present; in practice only one should be used")
                        for_demo2.append("error")
                        for_demo2.append(i[0])
                        for_demo2.append(i[1])
                        err_rule.append(for_demo2)

                else:
                    for_demo2=[]
                    for_demo2.append("ack003")
                    for_demo2.append("Acknowledgements")
                    for_demo2.append("The DTD allows multiple ce:acknowledgements to be present; in practice only one should be used")
                    for_demo2.append("no error")
                    err_rule.append(for_demo2)
            else:
                for_demo2=[]
                for_demo2.append("ack003")
                for_demo2.append("Acknowledgements")
                for_demo2.append("The DTD allows multiple ce:acknowledgements to be present; in practice only one should be used")
                for_demo2.append("no error")
                err_rule.append(for_demo2)
    except Exception as e:
        #print(e)
        for_demo2=[]
        for_demo2.append("ack003")
        for_demo2.append("Acknowledgements")
        for_demo2.append("The DTD allows multiple ce:acknowledgements to be present; in practice only one should be used")
        for_demo2.append("no error")
        err_rule.append(for_demo2)
        logging.info('='*50)
        logging.exception("Got exception on main handler in ack003 : Acknowledgements " )
        logging.shutdown()


    return err_rule

#file=r'E:\Desktop_files\RESUS_8162\RESUS-jss.xml'
#print(ack003(file))
