from bs4 import BeautifulSoup

def BRF037A(file_xml):
    rule_err = []
    error = []
    itemid='itemid'
    import logging
    from bs4 import BeautifulSoup
    try:
        with open(file_xml,"r",encoding= "utf-8") as f:    
            contents = f.read()    
        soup1 = BeautifulSoup(contents,"lxml")
        ce_ref = soup1.find_all("ce:bib-reference")
        for ele in ce_ref:
            for tags in ele.find_all(["sb:comment","ce:note"]):
                if (tags.name) == "sb:comment":
                    if len(tags.text.split()) > 3:
                        error.append(["text in sb:comment should come inside ce:note",contents.index(ele.attrs['id'])])
                if (tags.name) == "ce:note":
                    if len(tags.text.split()) <= 3:
                        error.append(["text in ce:note should come inside sb:comment",contents.index(ele.attrs['id'])])
        if error!=[]:
            for err in error:
                rule_file=[]
                rule_file.append("BRF037A")
                rule_file.append("Bibliographic references")
                rule_file.append("check if the end-note text is correctly identified")
                rule_file.append("error")
                rule_file.append(str(err[1]))
                rule_file.append(err[0])
                rule_err.append(rule_file)
        else:
            rule_file=[]
            rule_file.append("BRF037A")
            rule_file.append("Bibliographic references")
            rule_file.append("check if the end-note text is correctly identified")
            rule_file.append("no error")
            rule_err.append(rule_file)
    except Exception as e:
        print(e)
        rule_file=[]
        rule_file.append("BRF037A")
        rule_file.append("Bibliographic references")
        rule_file.append("check if the end-note text is correctly identified")
        rule_file.append("no error")
        rule_err.append(rule_file)
        logging.info('='*50)
        logging.exception("Got exception on main handler in BRF037A : Bibliographic references ")
        logging.shutdown()
    return rule_err# -*- coding: utf-8 -*-

#BRF037A(r"C:\Users\80044\Downloads\samples\YCTIM_102195\tx1.xml")
