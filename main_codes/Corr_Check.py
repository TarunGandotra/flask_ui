from bs4 import BeautifulSoup

def corr_check(filename1):
    main_file = []
    err_rule = []
    error=[]
    list_of_addr = []
    count=0
    with open(filename1, "r",encoding="utf-8") as f:
        contents = f.read()
        soup1 = BeautifulSoup(contents, 'lxml')        
        find = soup1.find("ce:correspondence")
        #print(find)
        if find == None:
            pass
        else:
            for j in find.find_all(recursive=False):
                
                if (j.name) == "sa:affiliation":
                    list_of_addr = (j.text.split("\n"))
                    list_of_addr = ([x for x in list_of_addr if x])
                
                elif j.name == "ce:text":
                    string_text = j.text
            
            if list_of_addr != []:
                for i in list_of_addr:
                    if i in string_text:
                        pass
                    else:
                        output = str(i)+" "+"is missing in address"
                        count+=1
            else:
                pass
    main_file.append("COR001")
    main_file.append("To check if affliation address and correspondence address contents are matching")    
    main_file.append("Corresponding address")
    if count == 0:
        for_demo2=[]
        for_demo2.append("UFA")
        for_demo2.append("aid")
        for_demo2.append("jid")
        for_demo2.append("no error")
        err_rule.append(for_demo2)
    else:
        for_demo2=[]
        for_demo2.append("ack003")
        for_demo2.append("acknowledgment")
        for_demo2.append("jid")
        for_demo2.append("error")
        for_demo2.append(str(contents.index("ce:correspondence")))
        for_demo2.append('affliation address and correspondence address contents are not matching')
        err_rule.append(for_demo2)

        
#         main_file.append("Failed")
#         main_file.append(output)
#         main_file.append("")
#         err_rule.append(main_file)   
    return err_rule
#filename1=r'C:\Users\Digiscape.THOMSON\Desktop\Digiscape\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\tx1.xml'
#filename1=r'C:\Users\Digiscape\Desktop\sindhu\MNT_ELSEVIER_JOURNAL_APCATA_17035_110\tx1.xml'
#print(corr_check(filename1))