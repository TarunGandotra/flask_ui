# -*- coding: utf-8 -*-
"""
Created on Fri May 17 14:49:58 2019

@author: Digiscape
# """
from fund_ref import fund
#from afn003 import AFN003
from Article_History import article_history
from BRX012 import Brx012
from rule_109 import Rule_109
from Che015 import CHE015_11
from rule_17 import Rule_17
from RULE_70 import rule_70
from rule_108 import Rule_108
from RULE_75 import rule_75
from Rule_39 import brx039
from Brx006 import BRX006
from Brx018 import BRX018
from RULE_83 import rule_83
from RULE_59 import rule_59
from RULE_7 import Rule_7
#from Corr_Check import corr_check    wrong ack003
from Rule_31_32 import rule31
from Rule_67 import rule_67
from Rule_66 import rule_66
from BRX041 import brx041
from Rule87 import rule_87
from Rule_08_new import Rule_08
from Brx005a import BRX005A
from BRX030 import brx030
from Rule_71 import rule_71
from Brf091b import BRF091B
from RULE40 import rule40
from BRX032 import brx032
from rule_91 import Rule_91
from Xstb702 import XsTB702
from Xstb701 import XsTB701
from Rule_27 import AEU001A
from Brx022 import BRX022
from BRF037A import Brf037a
from brx042 import Brx042
from BRX029B import brx029b
from Rule_73 import rule_73
from Table_Header import table_header
from Brx024 import BRX024
from rule30 import BRX001a
from Brx011 import BRX011
from Brx019 import BRX019
from HIS003A import rule_HIS003A
from Tab018 import tab018
from Brx005b_35 import BRX005B_35
from Rule89 import Rule_89
from RULE132 import rule132
from RULE_78_138 import rule_78_138
from RULE_113 import Rule_113
from AUG001 import aug001
from TableRule import Table
from rule_111 import Rule_111 
from Brx020b import BRX020B
from RULE_15_new import rule_15
from Brx007 import BRX007
#from TableRule import Table
from RULE_69 import rule_69
from Xsfm101 import XsFM101
from RULE135 import rule135
from afn003 import rule_afn003
from rule139_140 import Rule139_140
#from email_Vinay import Authors_Email
from Brx020a import BRX020A
from Aun009a import AUN009A
from Highlights import highlights
from rule_93 import Rule_93
from RULE41 import rule41
from RULE_79 import rule_79
from Rule_67 import rule_67
from RULE_80 import rule_80
from ack003_new import ack003
from  RULE_114 import Rule_114
from Keywords import keywords
from Label import label
from RULE_149 import Rule_149
from RULE_96 import Rule_96
from RULE_16 import rule_16
from rule_111 import Rule_111
from RULE_128 import Rule_128
from RULE120 import rule120
from Brx005b_36_37 import BRX005B_36
from AEU003 import aeu003
from RULE144 import rule144
from Afo002a import AFO002A
from RULE130 import rule130
from Xsfg601 import XsFG601
from TAIL import Tail
#from fund_ref import fund
from RULE116 import rule116
from TAB021 import tab021
from TAB012 import tab012
from RULE_72 import rule_72
from BRX010_42_43 import BRX010_42
from Rule_CHE045 import CHE_045
from Rule_FUN002 import FUN_002
from double_bond import CHE011
from ellip import Ellip
from fors5 import BRF033_
from note import BRF037A
from source import DQO002
from triple_bond import CHE011_tri
from app001 import APP001
from ABS004 import abs004



from bs4 import BeautifulSoup
import pypyodbc
import datetime
from shutil import copy2
import sys
import docx
import os
from datetime import date
import socket
import logging
from configparser import ConfigParser

def load_configuration(file_path):
    config = ConfigParser(allow_no_value=True)
    config.read(file_path)
    return config

config = load_configuration(r"C:\Users\digiscape\Desktop\batch\Batch_App_SmartQC\main_codes\file\settings.ini")
#print(config,'?'*100)
print(os.getcwd())

logging.basicConfig(filename=config["FILES"]["log"], filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
logger = logging.getLogger()
logging.info('   **-------Logger start from here-------**   '*4)
# config='C:\\Users\\digiscape\\Desktop\\log_file\\logger.log'
# logging.basicConfig(filename=config, filemode='a', format='%(asctime)s - %(message)s', level=logging.INFO)
# logger = logging.getLogger()
#print()
if len(sys.argv)>1: 
	path_for_file = sys.argv[1]
else:
	path_for_file = sys.argv[0]
print(sys.argv,'+'*50)
def update_db_master(updated_list):
        from datetime import datetime
        connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
        #connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=smart_qc;uid=sa;pwd=p@ssw0rd')
        cursor = connection.cursor()
        if(str(updated_list[7]!='null')):
            cursor.execute("UPDATE uniqmaster SET ERRORCOUNT ="+str(updated_list[1])+" "+",TIME_TAKEN_IN_SEC ="+str(updated_list[2])+" "+",true_positive ="+str(updated_list[3])+" "+",true_negative ="+str(updated_list[4])+" "+",false_positive ="+str(updated_list[5])+" "+",false_negative ="+str(updated_list[6])+" "+",BATCH_ID ="+str(updated_list[7])+" "+" "+" WHERE UNIQITEMID ="+"\'"+updated_list[0]+"\'"+";")
            cursor.execute("UPDATE uniqmaster SET USERID ="+"\'"+updated_list[8]+"\'"+" "+" WHERE UNIQITEMID ="+"\'"+updated_list[0]+"\'"+";")
        else:
            cursor.execute("UPDATE uniqmaster SET ERRORCOUNT ="+str(updated_list[1])+" "+",TIME_TAKEN_IN_SEC ="+str(updated_list[2])+" "+",true_positive ="+str(updated_list[3])+" "+",true_negative ="+str(updated_list[4])+" "+",false_positive ="+str(updated_list[5])+" "+",false_negative ="+str(updated_list[6])+" "+",BATCH_ID ="+str(updated_list[7])+" "+" "+" WHERE UNIQITEMID ="+"\'"+updated_list[0]+"\'"+";")
            cursor.execute("UPDATE uniqmaster SET USERID ="+"\'"+updated_list[8]+"\'"+" "+" WHERE UNIQITEMID ="+"\'"+updated_list[0]+"\'"+";")
        connection.commit()

        return


def insert_db_master(out_list):
        from datetime import datetime
        connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
        #connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=smart_qc;uid=sa;pwd=p@ssw0rd')
        cursor = connection.cursor()
        stmt_counter = "SELECT ARTICLE_EXECUTION_COUNTER FROM uniqmaster WHERE UNIQITEMID ="+"\'"+out_list[0]+"\'"+";"
        return_curs = cursor.execute(stmt_counter)

        k = return_curs.fetchone() 
        if k == None:
            params = ['?' for item in out_list]
            stmt= 'INSERT INTO uniqmaster (UNIQITEMID, USERID, JID, AID, STAGE,ITEMPROCESSINGDATE,ERRORCOUNT, ARTICLE_EXECUTION_COUNTER, ITEMPROCESSING_MODIFIED_DATE,TIME_TAKEN_IN_SEC) VALUES (%s);' % ','.join(params)
            cursor.execute(stmt, out_list)
        else:
            count = k[0]+1


            cursor.execute("UPDATE uniqmaster SET ERRORCOUNT ="+str(out_list[6])+" "+",TIME_TAKEN_IN_SEC ="+str(out_list[9])+" "+",ARTICLE_EXECUTION_COUNTER ="+str(count)+" "+",ITEMPROCESSING_MODIFIED_DATE = CONVERT(VARCHAR(50), getdate(),121) WHERE UNIQITEMID ="+"\'"+out_list[0]+"\'"+";")



            
        connection.commit()
        return
def insert_db_trans(out_list1):
    connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
    #connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=smart_qc;uid=sa;pwd=p@ssw0rd')
    cursor = connection.cursor()
    stmt_counter = "SELECT RULE_EXECUTION_COUNTER FROM uniqtransaction WHERE UNIQITEMID ="+"\'"+out_list1[0]+"\'"+" "+";"
    return_curs = cursor.execute(stmt_counter)

    k = return_curs.fetchone()
     
    if k == None:
        
        params = ['?' for item in out_list1]
        stmt= 'INSERT INTO uniqtransaction (UNIQITEMID, CATEGORY, RULEID, RULE_ERROR_DESC,RULE_EXECUTION_COUNTER) VALUES (%s);' % ','.join(params)
        cursor.execute(stmt, out_list1)
    else:
        
        #cursor.execute("UPDATE uniqtransaction SET RULE_EXECUTION_COUNTER = "+str(out_list1[-1])+" "+",RULE_ERROR_DESC = "+str(out_list1[-2])+" "+"WHERE UNIQITEMID ="+"\'"+out_list1[0]+"\'"+";")
        cursor.execute ("""
           UPDATE uniqtransaction
           SET RULE_EXECUTION_COUNTER=(?), RULE_ERROR_DESC=(?)
           WHERE UNIQITEMID=(?)
        """, (str(out_list1[-1]), str(out_list1[-2]), out_list1[0]))
    
    connection.commit()
    return  
def insert_db_smartqc_S5(out_list2):
        #connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=smart_qc;uid=sa;pwd=p@ssw0rd')
        connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
        cursor = connection.cursor()
        params = ['?' for item in out_list2]
        stmt = 'INSERT INTO smartqc_S5 (articleid, ruleid, true_positive, true_negative, false_positive,false_negative) VALUES (%s);' % ','.join(params)
        cursor.execute(stmt, out_list2)
        connection.commit()
        return            
def insert_db_error_count(error_count, itemid):
        #connection = pypyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=smart_qc;uid=sa;pwd=p@ssw0rd')
        connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
        cursor = connection.cursor()
        stmt = "UPDATE uniqmaster SET errorcount ="+" "+str(error_count)+" "+"WHERE  uniqitemid ="+"\'"+itemid+"\'"+";"
        cursor.execute(stmt)
        connection.commit()
        return         
def append_log(outlist, exists):
    for out_list in outlist:
        if out_list[3] == "no error":
            pass
        else:
            with open(exists, "r",encoding="utf-8") as f:
                contents = f.read()
                str_log = "<message id="+out_list[0]+" type= error"+" position=1:"+out_list[4]+">Error: "+out_list[5]+"</message>"
                soup1 = BeautifulSoup(contents,features="lxml")
                if soup1.results!=None:
                    soup1.results.append(BeautifulSoup(str_log,features="lxml"))
                f.close()
                
            with open(exists, "w",encoding="utf-8") as f:
                for i in soup1:
                    f.write(str(i))
                f.close()
    return

def Batch_S5(folderPath,batch_Id):
	try:
	    import time
	    Start_time = time.time()

	    #stage = "UNIQ_S5"
	    stage = config["STAGE"]["stage"]
	    print(stage,'stage?'*50)
	    path=folderPath
	    print(path)
	    #batchId = batch_Id
	    path_split = path.split("_")
	    print(path_split,'this is the split path')
	    print(path_split[-1])
	    if path_split[-1]=='110':
	        print('its in 110 block of batch'*5)
	        docx = "_".join(path_split[-3:-1])+".docx"
	        file_path = path.replace("\\","/")  + "/tx1.xml"
	        print(file_path,'this is the file path')
	        file = file_path.split('/')[-2].split("_")
	        print(file,'this is the file path for error rectification')    
	        jid = file[-3]
	        aid = file[-2]
	        itemid = jid+"_"+aid+"_"+stage
	        logging.info('   **-------Logger start from here for {}-------**   '.format(itemid))
	        time1 = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	        counter = 1
	        error_count = 0
	        uid = socket.gethostname()
	        exists =  os.path.isfile(path.replace("\\","/")+"/UNIQ_S5.xml")
	        jss_path = path.replace("\\","/")+"/"+jid+"-jss.xml"
	        order_path = path.replace("\\","/")+"/"+jid+"_"+aid+"_order.xml"
	        mss= path.replace("\\","/")+"/"+jid+"_"+aid+".docx"
	        tp=0
	        fp=0
	        tn=0
	        fn=0
	    else:
	        print('its not in 110 block of batch'*5)
	        docx = "_".join(path_split[-2:])+".docx"
	        file_path = path.replace("\\","/")  + "/tx1.xml"
	        print(file_path,'this is the file path')
	        file = file_path.split('/')[-2].split("_")
	        print(file,'this is the file path for error rectification')    
	        jid = file[-2]
	        aid = file[-1]
	        itemid = jid+"_"+aid+"_"+stage
	        logging.info('   **-------Logger start from here for {}-------**   '.format(itemid))
	        time1 = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	        counter = 1
	        error_count = 0
	        uid = socket.gethostname()
	        exists =  os.path.isfile(path.replace("\\","/")+"/UNIQ_S5.xml")
	        jss_path = path.replace("\\","/")+"/"+jid+"-jss.xml"
	        order_path = path.replace("\\","/")+"/"+jid+"_"+aid+"_order.xml"
	        mss= path.replace("\\","/")+"/"+jid+"_"+aid+".docx"
	        #mss = path+"/"+docx
	        #print('local path for mss2',mss2)
	        print('path for gen docx ',docx)
	        print('path for mss ',mss)
	        print('path for order ',order_path)
	        print('path for jss xml ',jss_path)
	        tp=0
	        fp=0
	        tn=0
	        fn=0

	#def Batch_S5(folderPath,batch_Id):
	#    import time
	#    Start_time = time.time()
	#
	#   stage = "UNIQ_S5"
	#    path=folderPath
	#    print(path)
	#    #batchId = batch_Id
	#    #path_split = path.split("_")
	#    path_split = path.split("\\")[-1].split("_")
	#    print(path_split,'this is the split path')
	#    #docx = "_".join(path_split[-3:-1])+".docx"
	#    docx = "_".join(path_split[-2:])+".docx"
	#    #copy2(path.replace("\\","/")+"/tx1.xml.log.xml",path.replace("\\","/")+"/UNIQ_S5.xml")
	#    file_path = path.replace("\\","/")  + "/tx1.xml"
	#    print(file_path,'this is the file path')
	#    file = file_path.split('/')[-2].split("_")
	#    print(file,'this is the file path for error rectification')    
	#    jid = file[-2]
	#    aid = file[-1]
	#    itemid = jid+"_"+aid+"_"+stage
	#    time1 = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	#    counter = 1
	#    error_count = 0
	#    uid = socket.gethostname()
	#    exists =  os.path.isfile(path.replace("\\","/")+"/UNIQ_S5.xml")
	#    jss_path = path.replace("\\","/")+"/"+jid+"-jss.xml"
	#    order_path = path.replace("\\","/")+"/"+jid+"_"+aid+"_order.xml"
	#    mss = path+"/"+docx
	#    tp=0
	#    fp=0
	#    tn=0
	#    fn=0
	    

	    
	    #print("starting path",path)
	    dest=r'E:\Desktop_files\TESTED FILES'
	    copy2(path.replace("\\","/")+"/tx1.xml.log.xml",dest.replace("\\","/")+"/temp_UNIQ_S5.xml")
	    #copy2(path+"\\tx1.xml.log.xml",path+"\\UNIQ_S5.xml")
	    #print("path",path)
	    log_path = dest.replace("\\","/")+"/temp_UNIQ_S5.xml"

	    Master_list = [itemid, uid, jid, aid, stage, time1, error_count, counter, time1, time.time()-Start_time]
	    insert_db_master(Master_list)

	    def log_transaction_db(obj,error_count,tp,tn,fp,fn):
	       append_log(obj,log_path)
	       tempdesc=""
	       ss=''
	       if 'error' in obj[0]:
	           ss=obj[0][-1]
	           error_count += len(obj)
	           tn+=1
	       else:
	           tp+=1
	       for sub in obj:
	          if "error" in sub:
	               #if(tempdesc==""):
	               #   tn+=1
	               #if(tempdesc!="" and sub[-1]!=tempdesc):
	               #    tn+=1
	               if (obj.index(sub)!=0):
	                  ss=ss+';'+sub[-1]    
	               #tempdesc=sub[-1]
	               #error_count+=1
	      
	       if 'error' in obj[0]:
	           trans_list=[itemid, obj[0][1], obj[0][0], ss, len(ss.split(';'))]
	           insert_db_trans(trans_list)
	       return error_count,tp,tn,fp,fn



	    obj = Brf037a(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'second one','Vinay')



	    obj = Rule_17(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'third one','vipin')


	    obj = rule_15(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'fourth one','vipin')


	    obj = Rule_08(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'sixth one','preeti')


	    obj = Rule_93(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'eight one','preeti')


	    obj = Rule_91(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'ninth one','preeti')

	    obj = AUN009A(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'eleventh one','shani')


	    obj = ack003(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'twelveth one','shani')


	    obj = Rule_108(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'thirteenth one','preeti')


	    obj = article_history(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'fourteenth one','Vipin')


	    obj = rule_59(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'fifteenth one','vipin')


	    obj = highlights(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'sixteenth one','shani')


	    obj = rule_87(file_path,order_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'seventeenth one','preeti')


	    obj = Rule_89(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'eighteenth one','preeti')


	    obj = rule_HIS003A(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'19th one','shani')


	    obj = rule_73(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'20th one','vipin')


	    obj = rule_66(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'21th one','vipin')

	    obj = rule_71(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'22th one','vipin')


	    obj = rule_67(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'23th one','vipin')


	    obj = aug001(file_path, mss)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'24th one','shani')


	    obj = BRX011(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'25th one','rachit')


	    obj = Brx042(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'26th one','kumar')


	    obj = brx039(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)

	    print(obj,'27th one','kumar')

	    obj = rule31(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'28th one','aditya')

	    obj = rule_afn003(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'29th one','shani')


	    obj = brx029b(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'30th one','kumar')


	    #obj = Table(file_path)
	    #error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    #print(obj,'31th one','shani')


	    obj = BRX007(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'31th one','aditya')


	    obj = BRX006(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'32th one','aditya')


	    obj = Table(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'33th one','shani')


	    obj = BRX018(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'34th one','rachit')

	    obj = BRX005A(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'35th one','aditya')

	    obj = brx030(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'36th one','kumar')


	    obj = brx041(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'37th one','kumar')


	    obj = BRX020A(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'38th one','rachit')


	    obj = brx032(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	##    append_log(obj,log_path)
	##    for sub in obj:
	##        if "error" in sub:
	##            error_count+=1
	##            trans_list=[jid+"_"+aid+"_"+"S5", itemid, sub[1], sub[0], sub[-1], counter]
	##            insert_db_trans(trans_list)
	    print(obj,'39th one','kumar')

	    obj = BRX001a(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'40th one','aditya')


	    obj = BRX019(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'41th one','rachit')


	    obj = BRX024(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'42th one','rachit')


	    obj = BRF091B(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'43th one','vipin')


	    obj = BRX005B_35(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'44th one','vipin')

	    obj = aeu003(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'45th one','kumar')


	    obj = BRX020B(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'46th one','rachit')


	    obj = AFO002A(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'47th one','preeti')


	    obj = BRX005B_36(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'48th and 49th one','vipin')

	    obj = tab018(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'50th ','kumar')


	    obj = XsTB701(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'51th','kumar')


	    obj = XsTB702(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'52th','kumar')


	    obj = BRX022(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'53th','rachit')


	    obj = Rule_114(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'54th','preeti')

	    obj = rule132(file_path, order_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'55th','rachit')


	    obj = rule40(file_path, mss)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'56th','aditya')



	    obj = Rule_113(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'57th','preeti')

	    obj = rule41(file_path, mss, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'58th','aditya')


	    obj = table_header(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'59th','shani')


	    obj = rule_80(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'60th','vipin')


	    obj = rule_72(file_path,jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'61th','vipin')


	    obj = rule_78_138(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'62th','vipin')


	    obj = Rule_111(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'63th','preeti')


	    obj = Rule_96(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'64th','preeti')

	    obj = label(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'65th','shani')

	    obj = keywords(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'66th','shani')

	    obj = Rule_109(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'67th','preeti')


	    #obj = Authors_Email(file_path, mss)
	    #error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    #print(obj,'68th','Vinay')



	    obj = Rule139_140(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'69th','aditya')

	    #obj = corr_check(file_path)
	    #error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    #print(obj,'70th','shani')  commented shani acl003 (151 UFA)


	    obj = rule_75(file_path, jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'71th','vipin')


	    obj = rule_69(file_path,mss, jss_path)
	    #print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",obj)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'72th','vipin')


	    obj = rule120(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'73th','aditya')


	    obj = rule_70(file_path,jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'74th','vipin')


	    obj = rule_79(file_path,jss_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'75th','vipin')


	    obj = rule_16(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'76th','vipin')

	    obj = rule_83(jss_path, file_path,order_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'77th','vipin')


	    obj = tab021( file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'78th','kumar')

	    obj = tab012(file_path, mss)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'79th','kumar')


	    obj = XsFG601(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'80th','kumar')

	    obj = XsFM101(file_path,order_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'81th','vipin')

	    obj = rule135(file_path, order_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'82th','rachit')


	    # obj = rule144(mss, file_path)
	    # error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    # print(obj,'83th','rachit')

	    # obj = rule130(file_path,json_path)
	    # append_log(obj,log_path)
	    # if "error" in obj:
	    #     error_count+=1
	    #     trans_list=[jid+"_"+aid+"_"+"S5", itemid, obj[2], obj[0], obj[-2], counter]
	    #     insert_db_trans(trans_list)
	    # print(obj,'84th','rachit')


	    obj = Rule_7(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'84th','preeti')

	    obj = rule116(file_path, mss)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'85th','aditya')

	    obj = Rule_149(file_path, mss)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'86th','preeti')

	    obj = Tail(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'87th','shani')

	    obj = Rule_128(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'88th','preeti')

	    obj = CHE015_11(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'89th','rachit')

	    obj = fund(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'90th','vinay')
	    
	    obj = AEU001A(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'91th','vipin')
	    
	    
	    obj = BRX010_42(jss_path,file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'92th','vipin')
	    
	    obj = CHE_045(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'93th','manisha')
	    
	    obj = FUN_002(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'94th','manisha')
	    
	    obj = FUN_002(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'94th','manisha')
	    
	    obj = CHE011(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'95th','Mayank')
	    
	    obj = Ellip(file_path,jss_path)
	    #print(obj)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'96th','Mayank')
	    
	    
	    obj = BRF033_(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'97th','Mayank')
	    
	    obj = BRF037A(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'98th','Mayank')
	    
	    obj = DQO002(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'99th','Mayank')
	    
	    obj = CHE011_tri(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'100th','Mayank')
	    
	    obj = APP001(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'101st','preeti')
	    
	    obj = abs004(file_path)
	    error_count,tp,tn,fp,fn,=log_transaction_db(obj,error_count,tp,tn,fp,fn)
	    print(obj,'102nd','preeti')
	    
	    
	    
	    copy2(dest.replace("\\","/")+"/temp_UNIQ_S5.xml",path.replace("\\","/")+"/UNIQ_S5.xml")

	    os.remove(dest.replace("\\","/")+"/temp_UNIQ_S5.xml")
	    updated_Master_list = [itemid, error_count, time.time()-Start_time,tp,tn,fp,fn,batch_Id,uid]
	    update_db_master(updated_Master_list)
	    #logging.info('\n\n')
	    logging.info('   **-------Logger End from here for {}-------**   '.format(itemid))
	    logging.info('\n\n')
	    logging.info('\n\n')
	except Exception as e:
		logging.info('=='*50)
		logging.exception('Got exception on main handler-----------')
		logging.info('\n\n')
		logging.shutdown()

	return

print(Batch_S5(path_for_file,"null"))
# folpath = 'C:/Users/80051/Desktop/uu'
# folpath = r'C:\Users\digiscape\Desktop\files_error\new_file'
# ldir = os.listdir(folpath)
# for i in ldir:
#        pth = folpath + '/' + i
#        print(Batch_S5(pth,'null'))
# print(Batch_S5("C:/Users/digiscape/Desktop/Dataset1/MNT_ELSEVIER_JOURNAL_CCLET_5021_110"))
