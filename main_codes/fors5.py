# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 10:16:36 2019

@author: 80044
"""

from bs4 import BeautifulSoup
import logging

def BRF033_(file_xml):
    rule_err = []
    error = []
    try:
        with open(file_xml,"r",encoding= "utf-8") as f:    
            contents = f.read()    
        soup1 = BeautifulSoup(contents,"lxml")
        ce_ref = soup1.find_all("ce:bib-reference")
        for ele in ce_ref:
            sta_coun = ele.find_all("ce:collaboration")
            if len(sta_coun)>0:
                error.append(["company names, government departments, etc., should be captured with the ce:surname element and not the ce:collaboration",contents.index(ele.attrs['id'])])
        if error!=[]:
            for err in error:
                rule_file=[]
                rule_file.append("BRF033")
                rule_file.append("Bibliographic references")
                rule_file.append("company names, government departments, etc., should be captured with the ce:surname element and not the ce:collaboration")
                rule_file.append("error")
                rule_file.append(err[0])
                rule_file.append(str(err[1]))
                rule_err.append(rule_file)
        else:
            rule_file=[]
            rule_file.append("BRF033")
            rule_file.append("Bibliographic references")
            rule_file.append("company names, government departments, etc., should be captured with the ce:surname element and not the ce:collaboration")
            rule_file.append("no error")
            rule_err.append(rule_file)
    except Exception as e:
        #print(e)
        rule_file.append("BRF033")
        rule_file.append("Bibliographic references")
        rule_file.append("company names, government departments, etc., should be captured with the ce:surname element and not the ce:collaboration")
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRF033 : Bibliographic references " )
        logging.shutdown()
    return rule_err
