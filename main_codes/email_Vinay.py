from bs4 import BeautifulSoup
import docx
def Authors_Email(file_xml, file_doc):
	e_mail = []
	error = []
	mail_id = []
	try:
		with open(file_xml,'r',encoding= "utf-8") as f:
			contents = f.read()
			#print(contents[10814:10830])    
			soup1 = BeautifulSoup(contents, 'lxml')
			for mail in soup1.find_all('ce:e-address'):
				#print(mail.text,'this is the inner text')
				diction = mail.attrs
				#print(diction)
				if diction['type'] == 'email':
					mail_id.append(mail.text) 

		lst = []
		doc = docx.Document(file_doc)
		for i in range(1,5):
			h = doc.paragraphs[i].text
			lst.append(h)
		lst = ' '.join(lst)
		#lst = lst.split()
		
		#print(lst,'list')
		for i in mail_id:
			if i not in lst:
				error.append(['AEU001A','Authors’ e-mail addresses/URLs','jid','error',str(contents.index(i)),'E-mail is not matching with the doc file'])
			else:
				pass
		if error == []:
			error.append(['AEU001A','Authors’ e-mail addresses/URLs','aid','no error'])
	except Exception as e:
		rule_file=[]
		rule_file.append('AEU001A')
		rule_file.append('Authors’ e-mail addresses/URLs')
		rule_file.append('jid')
		rule_file.append("no error")
		error.append(rule_file)


	return error


#file_xml = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\tx1.xml'
#file_doc = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\APCATA_17035.docx'
#print(Authors_Email(file_xml, file_doc))