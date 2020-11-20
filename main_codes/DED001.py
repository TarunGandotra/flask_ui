import nltk 
nltk.download('wordnet')
from nltk.corpus import wordnet
from bs4 import BeautifulSoup
def Rule_111(file):    
    for_demo2 = [] 
    synonyms = [] 
    
      
    for syn in wordnet.synsets("decease"):
        #print(syn,'fhjgjkgg') 
        for l in syn.lemmas(): 
            synonyms.append(l.name()) 
            
      
    #print(synonyms) 
    
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()
        soup1 = BeautifulSoup(contents, 'lxml')
        count = 0
        lst=[]
        try:
            for x in soup1.find_all('ce:dedication'):
                #print(x.text)
                z=x.text
                #print(z)
                lst.append(z)
                lst=(z.split())
                #print(lst)
            for i in lst:
                if i in synonyms:
                    count += 1
                else:
                    continue
            if count >= 1:
                for_demo2.append('DED001')
                for_demo2.append('jid')
                for_demo2.append('aid')
                for_demo2.append("error")
                for_demo2.append('ce:dedication indicating a deceased author')
                try:    
                    file = file.split('/')[-2]
                    #print(file)
                    file = file.split('_')   
                    JID_AID = file[-3]+"_"+file[-2]
                    #print(JID_AID)
                    for_demo2.insert(2,JID_AID )
                except IndexError:
                    a = 0+0        
                            
            else:
                for_demo2.append('DED001')
                for_demo2.append("null")
                for_demo2.append('pass')
                for_demo2.append("no error")
            

        except:
            for_demo2.append('DED001')
            for_demo2.append("null")
            for_demo2.append('pass')
            for_demo2.append("no error")        
    return for_demo2
       
        
#file =  r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\tx1.xml'
#print(Rule_111(file))