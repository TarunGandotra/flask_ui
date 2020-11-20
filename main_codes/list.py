from bs4 import BeautifulSoup
count = 0

with open(r'C:\Users\Digiscape\Desktop\sindhu\test\MNT_ELSEVIER_JOURNAL_APCATB_17604_110\fs.xml',encoding= "utf-8") as f:
    contents = f.read()
    soup = BeautifulSoup(contents,"lxml")
    for tag in soup.find_all("ce:abstract"):
        list_names = []
        for j in tag.descendants:
            list_names.append(j.name)    
        if "ce:list" and "ce:list-item" in list_names:
            print("True")
        else:
            print('error')