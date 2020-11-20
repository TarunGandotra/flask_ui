from bs4 import BeautifulSoup
def Rule_108(file):    
    for_demo2 = []
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()
        soup1 = BeautifulSoup(contents, 'lxml')
        count = 0
        list=[]
        list1=[]
    for x in soup1.find_all('ce:keywords'):
        #print(x.text)
        #print(x.attrs)
        for y in x.find_all('ce:section-title'):
            #print(y.text)
            v=y.text
            
            dict = (x.attrs)
            if dict['class'] == ['pubchem']:
                if v == 'chemical compounds studied in this article':
                    for_demo2.append('AFF011')
                    for_demo2.append("null")
                    for_demo2.append("no error")
                    print(True)
                else:
                    for_demo2.append('KEY007A')
                    for_demo2.append('jid')
                    for_demo2.append('aid')
                    for_demo2.append("error")
                    for_demo2.append( 'the text content of ce:section-title is not ‘Chemical compounds studied in this article’')
                  
            else:
                for_demo2.append('KEY007A')
                for_demo2.append('jid')
                for_demo2.append('aid')
                for_demo2.append("error")
                for_demo2.append('the text content of ce:section-title is not ‘Chemical compounds studied in this article’')
    try:    
        file = file.split('/')[-2]
        print(file)
        file = file.split('_')
            
        JID_AID = file[-3]+"_"+file[-2]
        #print(JID_AID)
        for_demo2.insert(2,JID_AID )
    except IndexError:
        pass
            
    return for_demo2
   
        
#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_INDCRO_11283_110/fs.xml'
#print(Rule_108(file))