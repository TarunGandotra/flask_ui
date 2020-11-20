import pyodbc
import pypyodbc
import pandas as pd
from configparser import ConfigParser

def load_configuration(file_path):
    config = ConfigParser(allow_no_value=True)
    config.read(file_path)
    return config

config = load_configuration(r"C:\Users\digiscape\Desktop\batch\Batch_App_SmartQC\main_codes\file\settings.ini")
def sqlquery(tablename,databasename):
	database=str(databasename)
	connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
	#connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database='+database+';uid=sa;pwd=p@ssw0rd')
	#cursor = connection.cursor()
	tbname=str(tablename)
	df=pd.read_sql_query("SELECT * FROM "+tbname,connection)
	#cursor.execute("SELECT * FROM Input1")
	return df

