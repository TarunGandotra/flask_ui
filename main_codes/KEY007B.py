from bs4 import BeautifulSoup
def Rule_109(file):    
    for_demo2 = []
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()
        soup1 = BeautifulSoup(contents, 'lxml')
        count = 0
        lst=[]
        list1=['CID:']
    for x in soup1.find_all('ce:keywords'):
       
        for y in x.find_all('ce:text'):
            #print(y.text)
            z = y.text
            lst=(z.split())
           # print(lst)
            
            
    result =  any(elem in lst for elem in list1)
    #print(result)
    if result:
        for_demo2.append('KEY007B')
        for_demo2.append("null")
        for_demo2.append('jid')
        for_demo2.append("no error")
           
    else :
        for_demo2.append('KEY007B')
        for_demo2.append('jid')
        for_demo2.append('aid')
        for_demo2.append("error")
        for_demo2.append("Does not include CID")
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
   
        
#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110/fs.xml'
#print(Rule_109(file)) 