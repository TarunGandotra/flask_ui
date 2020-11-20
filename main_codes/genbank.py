
# ncbi-wgs = ([A-Z]{1,2}[0-9]{1,2}[0-9\.?]{6,8})
#ncbi-n= ([A-Z]{1,2}[0-9\.?]{1,6})
#ncbi-p =([A-Z]{1,3}[0-9\.?]{1,5})
# ncbi-n=([NM|NT|NC|NG|XM|XR]{1,2}[_0-9\.?]{6,})
#ncbi-p = ([NP|XP|AP|ZP|YP]{1,2}\_[0-9\.?]{6,7})
# ncbi-mmdb = ([0-9]{1,5})
# ncbi-mga = ([A-Z]{1,5}[0-9\?]{1,7})
# ncbi-geo =([A-Z]{1,3}[0-9\?]{1,})
# CRAN=([[a-zA-Z0-9.\?]{1,})
# IGSN: HRV0035F0=([A-Z]{1,3}[[A-Z0-9\?]{1,7})
# FlyBase: FBgn0036925=([FB]{1,2}[gn|st]{1,2}[[0-9\?]{1,7})
# ncbi-tnm=([0-9\?]{1,4})
# ccdc=([A-Z]{1,2}[0-9\.?]{6,7})
# TAIR: AT1G01020=([AT]{1,2}[0-9]{1}[G]{1}[0-9\?]{1,6})
# OMIM: 601240 (or) MIM: 601240=([0-9\?]{1,6})
# MINT: 6166710=([0-9\?]{1,7})
# EMBL-EBI MI: 0218=([0-9\?]{1,4}) 
# UniProt: Q9H0H5 =([A-N|R-Z]{1}[0-9]{1}[A-Z]{1}[A-Z|0-9]{1}[A-Z]{1}[0-9\?]{1})  
# UniProt: Q9H0H5=([O|P|Q]{1}[0-9]{1}[A-Z]{1}[A-Z|0-9]{1}[A-Z|0-9]{1}[0-9\?]{1})
# PubMed/PMID: 19011746=([0-9\?]{1,8}) 
#  ASTM: G63 =([[A-Z0-9\?]{1,3})
# MGI: 2448567=([FB]{1,2}[gn|st]{1,2}[[0-9\?]{1,7})
# RRID: AB_204084=([AB]{1,2}[_]{1}[[0-9\?]{5,10})
# RGD: 1351014=([0-9\?]{1,7}) 
# wb-strain=([A-Z]{2,3}[0-9\?]{1,4})
# WB Protein=([WP]{1,2}[?:]{1}[CE]{1,2}[0-9\?]{1,5})
# wb-gene=([WBG]{1,3}[ene]{1,3}[0-9\?]{1,8})
# ZFIN: ZDB-GENO-960809-7=([ZDB]{1,3}[-]{1}[GENO|GENE|PUB|FISH]{1,4}[-]{1}[0-9\?]{1,6}[-]{1}[0-9\?]{1,5})
# geoscenic=([P]{1}[0-9\?]{6,7})
# eslide =([VM]{1,2}[0-9\?]{1,5})
# ascl =([0-9]{1,4}[.]{1}[0-9\?]{1,3})
# share Pattern=([a-zA-Z_0-9-]{1,}[.]{1}[vdi]{1,3})
# mycobank=([A-Z0-9]{1,7})
# array-express =([E|A]{1}[-]{1}[AFFY|AFMX|AGIL|ATMX|BAIR|BASE|BIOD|BUGS|CAGE|CBIL|DKFZ|EMBL|ERAD|FLYC|FPMI|GEHB|GEOD|GEUV|HGMP|IPKG|JCVI|JJRD|LGCL|MANP|MARS|MAXD|MEXP|MIMR|MNIA|MTAB|MUGN|NASC|NCMF|NGEN|RUBN|RZPD|SGRP|SMDB|SNGR|SYBR|TABM|TIGR|TOXM|UCON|UHNC|UMCU|WMIT]{1,4}[-]{1}[0-9\?]{1,})
# pride=([PXD]{1,3}[0-9\?]{1,6})
# afnd =([AFND]{1,4}[0-9\?]{1,6})
# fungidb=([A-Z]{1}[a-zA-Z0-9_]{1,})
# cryptodb =([a-zA-Z]{1}[A-Za-z0-9_.]{1,})
# toxodb=([a-zA-Z]{1}[A-Za-z0-9_.]{1,})
# pombase =([SP]{1,2}[A-Za-z0-9.]{1,})
# gsa=([CRA]{1,3}[0-9]{1,6})
# bioproject =([PRJCA]{1,5}[0-9]{1,6})
# rridsoftware=([SCR]{1,3}[_]{1}[0-9]{5,})
# pcddb= ([CD]{1,2}[0-9]{1,7}[0-9]{1,3})
from bs4 import BeautifulSoup
import re
xml = 'C:/Users/Digiscape/Desktop/Digiscape/VIRMET_13660.xml'
def GenBank(xml):

	with open(xml,'r',encoding = 'utf-8') as f:
		contents = f.read()
		soup = BeautifulSoup(contents,'lxml')
		for section in soup.find_all('ce:section'):
			for inter in section.find_all('ce:inter-ref'):
				dict1 = inter.attrs
				print(dict1['xlink:href'],'this is dictionary')
				pat_p = re.findall('[NP|XP|AP|ZP|YP]{1,2}\_[0-9\.?]{6,7}', dict1['xlink:href'])
				pat_p = ''.join(pat_p)
				print(pat_p,'this is pat_p')
				pat_n = re.findall('[NP|XP|AP|ZP|YP]{1,2}[_0-9\.?]{1,9}', dict1['xlink:href'])
				pat_n = ''.join(pat_n)
				print(pat_n,'this is pat_n') 
				pat_wgs = re.findall('[NP|XP|AP|ZP|YP]{1,2}[0-9\.?]{1,9}',dict1['xlink:href'])
				pat_wgs = ''.join(pat_wgs)
				print(pat_wgs,'this is pat_wgs')
				if 'ncbi-wgs' in dict1['xlink:href']:
					if pat_wgs in dict1['xlink:href']:
						if inter.text in dict1['xlink:href']:
							print('no error')
						else:
							print('error')
				elif 'ncbi-p' in dict1['xlink:href']:
					print('pat_p ke upar')
					if pat_p in dict1['xlink:href']:
						print('inter ke upar for pat_p')
						if inter.text in dict1['xlink:href']:
							print('no error')
						else:
							print('error')
				elif 'ncbi-n' in dict1['xlink:href']:
					if pat_n in dict1['xlink:href']:
						if inter.text in dict1['xlink:href']:
							print(pat_n, inter.text)
							print('no error')
						else:
							print('error')
					else:
						print('error')
				else:
					print('error')






print(GenBank(xml))


