import pyodbc
import pypyodbc
import pandas as pd
from configparser import ConfigParser

def load_configuration(file_path):
    config = ConfigParser(allow_no_value=True)
    config.read(file_path)
    return config

config = load_configuration(r"C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\main_codes\file\settings.ini")
def sqlquery_AS(tablename,databasename):
	database=str(databasename)
	connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
	#connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database='+database+';uid=sa;pwd=p@ssw0rd')
	#cursor = connection.cursor()
	tbname=str(tablename)
	df=pd.read_sql_query("select uniqitemid as 'ITEM_ID', userid as 'USER_ID', jid as 'JOURNAL_ID' , aid as 'ARTICLE_ID' , stage , itemprocessingdate as 'ARTICLE_PROCESS_DATE',errorcount as 'ERROR_COUNT',article_execution_counter as 'EXECUTION_COUNTER' ,time_taken_in_sec as 'EXECUTION_TIME', itemprocessing_modified_date  as 'MODIFIED_DATE' from uniqmaster where stage like'UNIQ_S5%'",connection)
	#cursor.execute("SELECT * FROM Input1")
	df.columns = [x.upper() for x in df.columns]
	return df

def sqlquery_CE(tablename,databasename):
	database=str(databasename)
	connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
	#connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database='+database+';uid=sa;pwd=p@ssw0rd')
	#cursor = connection.cursor()
	tbname=str(tablename)
	df=pd.read_sql_query("select uniqitemid as 'ITEM_ID', userid as 'USER_ID', jid as 'JOURNAL_ID' , aid as 'ARTICLE_ID' , stage , itemprocessingdate as 'ARTICLE_PROCESS_DATE',errorcount as 'ERROR_COUNT',article_execution_counter as 'EXECUTION_COUNTER' ,time_taken_in_sec as 'EXECUTION_TIME', itemprocessing_modified_date  as 'MODIFIED_DATE' from uniqmaster where stage like'UNIQ_CE%'",connection)
	#cursor.execute("SELECT * FROM Input1")
	df.columns = [x.upper() for x in df.columns]
	return df

def sqlquery_CNU(tablename,databasename):
	database=str(databasename)
	connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
	#connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database='+database+';uid=sa;pwd=p@ssw0rd')
	#cursor = connection.cursor()
	tbname=str(tablename)
	df=pd.read_sql_query("select uniqitemid as 'ITEM_ID', userid as 'USER_ID', jid as 'JOURNAL_ID' , aid as 'ARTICLE_ID' , stage , itemprocessingdate as 'ARTICLE_PROCESS_DATE',errorcount as 'ERROR_COUNT',article_execution_counter as 'EXECUTION_COUNTER' ,time_taken_in_sec as 'EXECUTION_TIME', itemprocessing_modified_date  as 'MODIFIED_DATE' from uniqmaster where stage like'UNIQ_CU%'",connection)
	#cursor.execute("SELECT * FROM Input1")
	df.columns = [x.upper() for x in df.columns]
	return df


def sqlquery_Art(tablename,databasename):
	database=str(databasename)
	connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
	#connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database='+database+';uid=sa;pwd=p@ssw0rd')
	#cursor = connection.cursor()
	tbname=str(tablename)
	df=pd.read_sql_query("select uniqitemid as 'ITEM_ID', userid as 'USER_ID', jid as 'JOURNAL_ID' , aid as 'ARTICLE_ID' , stage , itemprocessingdate as 'ARTICLE_PROCESS_DATE',errorcount as 'ERROR_COUNT',article_execution_counter as 'EXECUTION_COUNTER' ,time_taken_in_sec as 'EXECUTION_TIME',img_count_bw as 'BW_images',img_count_color as 'COLOURED_IMAGES', itemprocessing_modified_date  as 'MODIFIED_DATE' from uniqmaster where stage like'UNIQ_ART%'",connection)
	#cursor.execute("SELECT * FROM Input1")
	df.columns = [x.upper() for x in df.columns]
	return df