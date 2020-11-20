# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 14:25:55 2019

@author: 80044
"""

from bs4 import BeautifulSoup
import logging
def Ellip(file_xml,jss):
    error = []
    rule_err = []
    try:
        with open(jss, "r",encoding="utf8") as f:
            contents1 = f.read()    
        soup = (BeautifulSoup(contents1, 'lxml'))
        for i in soup.find_all("refstyle"):
            
            if "APA" in i.text:
                with open(file_xml, "r",encoding="utf8") as f:
                    contents = f.read()    
                soup = (BeautifulSoup(contents, 'lxml'))
                check_for_ellip_ver = soup.find_all("sb:ellipsis")
                if check_for_ellip_ver !=[]:
                    tags_for_bib = soup.find_all("ce:bib-reference")
                    for i in tags_for_bib:
                        for j in i.find_all("sb:authors"):
                            no_of_authors = j.find_all("ce:given-name")
                            if len(no_of_authors) > 7:
                                error.append(["Eight or more authors should be replaced with ellipsis between first six and the last author",contents.index(i.attrs['id'])])
                        
        if error!=[]:
            for err in error:
                rule_file=[]
                rule_file.append("BRX028")
                rule_file.append("Checking for closed bracket with year in cross-ref and unique cross- ref according to the author's names")
                rule_file.append("Bibliographic reference cross-references")
                rule_file.append("error")
                rule_file.append(err[0])
                rule_file.append(str(err[1]))
                rule_err.append(rule_file)
        else:
            rule_file=[]
            rule_file.append("BRX028")
            rule_file.append("Bibliographic reference cross-references")
            rule_file.append("Checking for closed bracket with year in cross-ref and unique cross- ref according to the author's names")
            rule_file.append("no error")
            rule_err.append(rule_file)
    except Exception as e:
        print(e)
        rule_file=[]
        rule_file.append("BRX028")
        rule_file.append("Bibliographic reference cross-references")
        rule_file.append("Checking for closed bracket with year in cross-ref and unique cross- ref according to the author's names")
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRX028 : Bibliographic reference cross-references " )
        logging.shutdown()
    return rule_err
#with open(r"\\172.16.1.146\share\backup\MNT_ELSEVIER_JOURNAL_AIP_1532_110\tx1.xml", "r",encoding="utf8") as f:
#    contents = f.read()   
#ellip(contents,r"\\172.16.1.146\share\backup\MNT_ELSEVIER_JOURNAL_AIP_1532_110\AIP-jss.xml")            
