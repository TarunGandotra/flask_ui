from bs4 import BeautifulSoup
import logging

def abs004(file):
    rule_err =[]
    error=[]
    lst1 =['Highlights','Research Highlights']
    try:
        with open(file,'r',encoding = 'utf-8') as f:
            contents = f.read()
            #print(contents[22992:23000])
            soup = BeautifulSoup(contents,'lxml')
            for i in soup.find_all('ce:abstract'):
        #         print(i.attrs)
        #         print(type(i.attrs))

                thisdict = i.attrs
                for x in thisdict:

                    if x == 'class':
                        pass
                        if thisdict[x] == ['author-highlights']:
                            pass
                            for j in i.find_all('ce:section-title'):
                                pass
                                if j.text in lst1:
                                    pass
                                else:
                                    error.append([str(contents.index(j.text)),'‘Research highlights’ or ‘Highlights’ and the section title supplied should not be used'])
                        else:
                            pass
                    else:
                        pass
        if error!=[]:
            for err in error:
                rule_file=[]
                rule_file.append('ABS004')
                rule_file.append("Abstracts and highlights")
                rule_file.append("‘Research highlights’ or ‘Highlights’ and the section title supplied should not be used")
                rule_file.append("error")
                rule_file.append(err[0])
                rule_file.append(str(err[1]))
                rule_err.append(rule_file)
        else:
                rule_file=[]
                rule_file.append('ABS004')
                rule_file.append("Abstracts and highlights")
                rule_file.append("Research highlights’ or ‘Highlights’ and the section title supplied should be used")
                rule_file.append("no error")
                rule_err.append(rule_file)            
    except Exception as e:
        rule_file=[]
        rule_file.append('ABS004...')
        rule_file.append("Abstracts and highlights")
        rule_file.append(" ‘Research highlights’ or ‘Highlights’ and the section title supplied should be used ")
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in ABS004 : Abstracts and highlights " )
        logging.shutdown()
                        
    return rule_err
   
        
#file = r'C:\Users\digiscape\Desktop\TESTED FILES\NANTOD_100795_Abs004\tx1.xml'            

#print(abs004(file))             
                
                
