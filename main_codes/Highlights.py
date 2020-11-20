from bs4 import BeautifulSoup
import logging
count = 0
def highlights(file):
    err_rule=[]
    error=[]
    try:
        with open(file,'r',encoding= "utf-8") as f:
            contents = f.read()
            soup = BeautifulSoup(contents,"lxml")
            for i in soup.find_all("ce:abstract"):
                for j in i.find_all('ce:section-title'):
                    #print(j.find('ce:list-item'))
                    if j.text=='Highlights':
                        #print(i)
                        if i.find("ce:list") and i.find("ce:list-item"):
                            print("no error")
                        else:
                            error.append([str(contents.index(Highlights)),"ce:list and ce:list-item is not present"])
                            print("error")

            if error!=[]:
                for i in error:
                    #print('error')
                    for_demo2=[]
                    for_demo2.append("ABS006A")
                    for_demo2.append("Abstracts and highlights")
                    for_demo2.append("The highlights should be captured in a ce:list structure")
                    for_demo2.append("error")
                    for_demo2.append(i[0])
                    for_demo2.append(i[1])
                    err_rule.append(for_demo2)
            else:
                for_demo2=[]
                for_demo2.append("ABS006A")
                for_demo2.append("Abstracts and highlights")
                for_demo2.append("The highlights should be captured in a ce:list structure")
                for_demo2.append("no error")
                err_rule.append(for_demo2)
    except Exception as e:
        for_demo2=[]
        for_demo2.append("ABS006A")
        for_demo2.append("Abstracts and highlights")
        for_demo2.append("The highlights should be captured in a ce:list structure")
        for_demo2.append("no error")
        err_rule.append(for_demo2)
        logging.info('='*50)
        logging.exception("Got exception on main handler in ABS006A : Abstracts and highlights " )
        logging.shutdown()
    return err_rule
#file = r'C:/Users/Digiscape/Desktop/sindhu/MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(highlights(file))

