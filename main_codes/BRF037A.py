from bs4 import BeautifulSoup

def Brf037a(file):
	lst = []
	for_demo2 = []
	count = 0
	with open(file,'r',encoding = 'utf-8') as f:
		contents = f.read()
		soup = BeautifulSoup(contents, 'lxml')
		for note in soup.find_all('ce:bib-reference'):
			for comment in note.find_all('sb:comment'):
				lst.append(comment.text)
	#print(lst)

	for i in lst:
		if i!='' and (i in contents):
			if len(i.split()) >=10:
				count += 1
				for_demo2.append(['BRF037A','AID','JID','error',str(contents.index(i)),'Chances that it might come in ce:note'])
			else:
				pass
	if count == 0:
		for_demo = []
		for_demo.append('BRX012')	
		for_demo.append('AID')
		for_demo.append('JID')
		for_demo.append('no error')
		for_demo2.append(for_demo)
	return for_demo2

#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(Brf037a(file))