# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:23:45 2019

@author: 80044
"""

import re
import logging

def CHE011(file_xml):
    rule_err = []
    error = []
    try:
        with open(file_xml,"r",encoding= "utf-8") as f:    
            contents = f.read()    
        p = re.compile('[C|O|N|P]=[C|O|N|P]')
        
        for j in re.finditer(p,contents):
            error.append(["The double bond glyph ce:glyph should be used to indicate a double bond, and not the equivalent sign ‘=’",j.start()])
        if error!=[]:
            for err in error:
                rule_file=[]
                rule_file.append("CHE011")
                rule_file.append("Chemistry")
                rule_file.append("The double bond glyph ce:glyph should be used to indicate a double bond, and not the equivalent sign ‘=’")
                rule_file.append("error")
                rule_file.append(err[0])
                rule_file.append(str(err[1]))
                rule_err.append(rule_file)
        else:
            rule_file=[]
            rule_file.append("CHE011")
            rule_file.append("Chemistry")
            rule_file.append("The double bond glyph ce:glyph should be used to indicate a double bond, and not the equivalent sign ‘=’")
            rule_file.append("no error")
            rule_err.append(rule_file)
    except Exception as e:
        print(e)
        rule_file=[]
        rule_file.append("CHE011")
        rule_file.append("Chemistry")
        rule_file.append("The double bond glyph ce:glyph should be used to indicate a double bond, and not the equivalent sign ‘=’")
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in CHE011 : Chemistry " )
        logging.shutdown()
        
    return rule_err
#CHE011(r"C:\Users\80044\Downloads\samples\GAIPOS_7359\tx1.xml")
