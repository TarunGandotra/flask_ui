from bs4 import BeautifulSoup
import re
import logging
def AUN009A(file):
	#for_demo2 = []
	err_rule=[]
	for_demo2=[] 
	count = 0
	lst=[]
	try:
		with open(file,'r',encoding ='utf-8') as f:
		#with open(r'C:\Users\Digiscape.THOMSON\Desktop\Digiscape\xml\MNT_ELSEVIER_JOURNAL_APCATB_17604_110\fs.xml',"r",encoding= "utf-8") as f:
			contents = f.read() 
			#print(contents[4848:4900])   
			soup = BeautifulSoup(contents,"lxml")
			#print(contents[4848:4900])
			for k in soup.findAll('ce:given-name'):
				#print(k,"$$$$$$$$$$$$$$$$$$$$$$$$$$")
				for i in k.text:
					#print(k.text.isascii())
					if not(ord(i)<=400 and ord(i)>=0):
						for_demo2.append("AUN009A")
						for_demo2.append("Author names")
						for_demo2.append("Author names are sometimes given in their native language in addition to the principal language of the article")
						for_demo2.append("error")
						for_demo2.append(str(contents.index('ce:given-name')))
						for_demo2.append("native language name comes in given-name")
						err_rule.append(for_demo2)
						break;
			if(for_demo2==[]):
				for_demo2=[]
				for_demo2.append("AUN009A")
				for_demo2.append("Author names")
				for_demo2.append("Author names are sometimes given in their native language in addition to the principal language of the article")
				for_demo2.append("no error")
				err_rule.append(for_demo2)
	except Exception as e:
		for_demo2=[]
		for_demo2.append("AUN009A")
		for_demo2.append("Author names")
		for_demo2.append("Author names are sometimes given in their native language in addition to the principal language of the article")
		for_demo2.append("no error")
		err_rule.append(for_demo2)
		logging.info('='*50)
		logging.exception("Got exception on main handler in AUN009A : Author names " )
		logging.shutdown()
	return err_rule
#file = r'C:/Users/digiscape/Desktop/DataSet1/MNT_ELSEVIER_JOURNAL_ACTROP_5038_110/tx1.xml'
#print(AUN009A(file))
