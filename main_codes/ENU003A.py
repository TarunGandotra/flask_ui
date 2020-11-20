from bs4 import BeautifulSoup


def Rule_91(file):
    for_demo2 = []
    with open(file, 'r', encoding='utf-8') as f:
        contents = f.read()
        soup1 = BeautifulSoup(contents, 'lxml')
        count = 0
        lst=[]
        lst2=[]
        
    for x in soup1.find_all('ce:sections'):
        for y in x.find_all('ce:enunciation'):
            for z in y.find_all('ce:label'):
                print(z.text)
                lst.append(z.text)
                print(lst)
            #print(len(lst))
            for i in range(1, len(lst)+1):
               
                claims = 'Claim {}'.format(i)
                Conjecture = 'Conjecture {}'.format(i)
                Corollaries = 'Corollary {}'.format(i)
                Lemma  = 'Lemma {}'.format(i)
                Properties = 'Property{}'.format(i)
                Preposition = 'Preposition {}'.format(i)
                Theorem = 'Theorem {}'.format(i)
                lst2.append(claims)
                lst2.append(Conjecture)
                lst2.append(Corollaries)
                lst2.append(Lemma)
                lst2.append(Properties)
                lst2.append(Preposition)
                lst2.append(Theorem)
            #print(lst2)
            
        for i in lst:
            if i in lst2:
                continue
            else:
                count += 1
        if count >= 1:
            for_demo2.append('ENU003A')
            for_demo2.append('jid')
            for_demo2.append('aid')
            for_demo2.append("error")
            for_demo2.append('Claims, Conjectures, Corollaries, Lemmas, Properties, Propositions and Theorems captured with ce:enunciation')
        else:
            for_demo2.append('ENU003A')
            for_demo2.append("null")
            for_demo2.append('jid')
            for_demo2.append("no error")

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
   
        
#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_INDCRO_11283_110\fs.xml'
#print(Rule_91(file))