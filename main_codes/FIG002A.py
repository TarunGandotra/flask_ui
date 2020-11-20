from bs4 import BeautifulSoup

def Rule_93(file):
    rule_err = []
    error = []
    list1=[]
    lst2 =[]
    count = 0
    try:
        with open(file, 'r', encoding='utf-8') as f:
            contents = f.read()
            soup1 = BeautifulSoup(contents, 'lxml')
            
           
            
            
            for x in soup1.find_all('ce:figure'):
                for y in x.find_all('ce:label'):
                   # print(y.text)
                    list1.append(y.text)
                    
                    #for substring in list1: 
        
           # print(len(list1))
            
            #for i in list1:
            for i in range(1, len(list1)+1):
                scheme = 'Scheme {}'.format(i)
                fig = 'Fig. {}'.format(i)
                figs = 'Figure {}'.format(i)
                plate = 'plate {}'.format(i)
                lst2.append(scheme)
                lst2.append(figs)
                lst2.append(fig)
                lst2.append(plate)
           # print(lst2)
        
            for i in list1:
                if i not in lst2:
                    #print(i)
                    error.append([str(contents.index(i)),'label does not contain the designations that are mandatory i.e plate, fig. scheme'])
                else:
                    continue
            if error!=[]:
                    for err in error:
                        rule_file=[]
                        rule_file.append('FIG002A')
                        rule_file.append("Figures")
                        rule_file.append('ce: label does not contain the designations that are mandatory i.e plate, fig. scheme')
                        rule_file.append("error")
                        rule_file.append(err[0])
                        rule_file.append(str(err[1]))
                        rule_err.append(rule_file)
            else:
                rule_file=[]
                rule_file.append('FIG002A')
                rule_file.append("Figures")
                rule_file.append("ce: label contain the designations that are mandatory i.e plate, fig. scheme'")
                rule_file.append("no error")
                rule_err.append(rule_file)
    except Exception as e:
        rule_file.append('FIG002A')
        rule_file.append("Figures")
        rule_file.append("ce: label contain the designations that are mandatory i.e plate, fig. scheme'")
        rule_file.append("no error")
        rule_err.append(rule_file)
        
                
    return rule_err
   
        
#file = r'C:\Users\digiscape\Desktop\TESTED FILES\AS\AAP_5213\tx1.xml'
#print(Rule_93(file)) 
