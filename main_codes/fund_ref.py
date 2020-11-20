
import pandas as pd
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process
# import ConfigParser
from configparser import ConfigParser

def load_configuration(file_path):
    config = ConfigParser(allow_no_value=True)
    config.read(file_path)
    #print(config)
    return config

def fund(file):
	''' This is the csv file which contains List of Companies and their respective ID's'''
	for_demo2 = []
	try:
		
		config = load_configuration("settings.ini")	
		df = pd.read_csv(config["PATH"]["path"])
		questions = []
		Companies = []
		questions.append(zip(df['orgDbId'], df['preferredOrgName'] ))
		Ques_Ans = set(*questions)
		dict1 = dict(Ques_Ans)
		for k, v in dict1.items():
			Companies.append(v)



		dict2 = {}
		Extracted_Companies = []
		with open(file,'r', encoding ='utf-8') as f:
			contents = f.read()
			soup = BeautifulSoup(contents, 'lxml')
			for ack in soup.find_all('ce:acknowledgment'):
				for granSpon in ack.find_all('ce:grant-sponsor'):
					dict_ = granSpon.attrs
					dict2[dict_['id']] =  granSpon.text
					Extracted_Companies.append(granSpon.text)
		
			count = 0
			counter = 0

			
			matched_dict = {}
			for k2, v2 in dict2.items():
				max_score = 0.0
				if k2.startswith('gs') :
					continue
				else:
					for k1, v1 in dict1.items():
						temp_score = fuzz.ratio(v2,v1)
						if temp_score > max_score:
							max_score = temp_score
							matched_dict[v2] = [int(k2),k1,contents.index(k2),contents.index(v2),temp_score]

			count = 0
			count_keys = 0
			for k,v in matched_dict.items():
				if v[4] < 90:
					count += 1
					for_demo2.append(['Fund_rule','null','pass',str(v[3]),'error','company name not found in list'])

				if v[0] != v[1]:
					count += 1
					for_demo2.append(['Fund_rule','null','pass',str(v[2]),'error','company id not found in list']) 
					continue
			
			if count == 0:
				for_demo = []
				for_demo.append('fund_rules')	
				for_demo.append('AID')
				for_demo.append('JID')
				for_demo.append('no error')
				for_demo2.append(for_demo)
	except Exception as e:
		for_demo = []
		for_demo.append('fund_rules')	
		for_demo.append('AID')
		for_demo.append('JID')
		for_demo.append('no error')
		for_demo2.append(for_demo)



	return for_demo2

    

#file = r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110/tx1.xml'
#print(fund(file))




# ''' Here we are comparing the output of csv with the XML. If True then pass orelse prompt an error for the same.'''
# ''' Here we get the Company Names and their ID's extarcted from the csv file'''
