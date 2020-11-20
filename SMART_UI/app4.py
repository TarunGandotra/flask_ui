from flask import Flask,render_template,url_for,request
import os
import pandas as pd 
import pickle
import sys
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.externals import joblib
from werkzeug import secure_filename
from datetime import date
import time
import pyodbc
from sqlquery import sqlquery
from sqlquery_AS import *
import re
import socket
import data_image
import requests

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
APP_ROOT=os.getcwd() 
x=100
table=pd.DataFrame()

@app.route('/',methods= ['GET'])
def himanshu():
	import data_image
	# userId = request.form['uname']
	# password = request.form['psw']
	# if userId == 'admin' and password == 'p@ssw0rd':
	# 	return render_template('home.html')
	# else:
	# 	return render_template('loging1.html')
	return render_template('loging1.html')



@app.route('/home',methods=['GET','POST'])
def home():
	import data_image
	userId=request.args["uname"]
	# userId = request.form['uname']
	password=request.args["psw"]
	if userId != "admin" or password != "admin":
		# return render_template('home.html')
		return render_template('loging1.html')
	else:
		#return redirect(url_for('home'))
		return render_template('home.html')
	return render_template('home.html')

@app.route('/backHome',methods=['GET','POST'])
def backHome():
	import data_image
	# userId=request.args["uname"]
	# # userId = request.form['uname']
	# password=request.args["psw"]
	# if userId != "admin" or password != "admin":
	# 	# return render_template('home.html')
	# 	return render_template('loging1.html')
	# else:
	# 	#return redirect(url_for('home'))
	# 	return render_template('home.html')
	return render_template('home.html')


#function for date submit from home page
@app.route('/date_home',methods=['GET','POST'])
def date_home():
	date = request.args["birthday"]
	print("date for the birthday is "+str(date))
	import data_image_for_date
	data_image_for_date.date_data_image(date)

	# userId = request.form['uname']
	
	# password = request.form['psw']
	# if userId != "admin" or password != "admin":
	# 	# return render_template('home.html')
	# 	return render_template('loging1.html')
	# else:
	# 	#return redirect(url_for('home'))
	# 	return render_template('home.html')
	return render_template('home.html')

@app.route('/batch')
def batch():
	return render_template('batch.html')

@app.route('/Smartq_AS')
def Smartq_AS():
	tablename='uniqmaster'
	databasename='smart_qc'
	global table
	table=sqlquery_AS(tablename,databasename)
	table2=pd.DataFrame(table)
	table2=table2.astype('str')
	return render_template('data.html',data='UNIQS5',table=table2,table1=table2[x-100:x].to_html(),page=int(x/100))
	#return "<h1>Work in procces for Smartq_AS.#Vipin</h1>"

@app.route('/Smartq_CE')
def Smartq_CE():
	tablename='uniqmaster'
	databasename='smart_qc'
	global table
	table=sqlquery_CE(tablename,databasename)
	table2=pd.DataFrame(table)
	table2=table2.astype('str')
	return render_template('data.html',data='UNIQCE',table=table2,table1=table2[x-100:x].to_html(),page=int(x/100))
	#return "<h1>Work in procces for Smartq_AS.#Vipin</h1>"

@app.route('/Smartq_CNU')
def Smartq_CNU():
	tablename='uniqmaster'
	databasename='smart_qc'
	global table
	table=sqlquery_CNU(tablename,databasename)
	table2=pd.DataFrame(table)
	table2=table2.astype('str')
	return render_template('data.html',data='UNIQCU',table=table2,table1=table2[x-100:x].to_html(),page=int(x/100))
	#return "<h1>Work in procces for Smartq_AS.#Vipin</h1>"

@app.route('/Uniq_Art')
def Uniq_Art():
	tablename='uniqmaster'
	databasename='smart_qc'
	global table
	table=sqlquery_Art(tablename,databasename)
	table2=pd.DataFrame(table)
	table2=table2.astype('str')
	return render_template('data.html',data='UNIQART',table=table2,table1=table2[x-100:x].to_html(),page=int(x/100))
	#return "<h1>Work in procces for Smartq_AS.#Vipin</h1>"

@app.route('/data_report',methods=['POST'])
def data_report():
	tablename=request.form['TableName']
	databasename=request.form['DatabaseName']
	global table
	table=sqlquery(tablename,databasename)
	table2=pd.DataFrame(table)
	table2=table2.astype('str')
	return render_template('data.html',table=table2,table1=table2[x-100:x].to_html(),page=int(x/100))


@app.route('/data_report_page',methods=['POST'])
def data_page():
	global table
	page=request.form['PageNo.']
	page=int(re.findall('\d+',page)[0])
	table2=pd.DataFrame(table)
	if(100*(page)<len(table2.index)):
		x=100*(page-1)
		y=100*page
	elif(100*(page-1)>len(table2.index)):
		return render_template('goback.html')
	else:
		x=100*(page-1)
		y=len(table2.index)

	table2=table2.astype('str')
	return render_template('datapg.html',table=table2,table1=table2[x:y].to_html(),page=page)

w=100
@app.route('/data_report_sorted',methods=['POST'])
def sorted_data():
	global sorte
	global order
	sorte=request.form['column']
	order=request.form['order']
	global table
	table2=pd.DataFrame(table)
	table2=table2.sort_values([str(sorte)],ascending=('Ascending'==order))
	table2=table2.astype('str')
	return render_template('sorted.html',table=table2,table1=table2[:100].to_html(),page=int(w/100))



@app.route('/data_sort_page',methods=['POST'])
def sort_page():
	global table
	global sorte
	global order
	page=request.form['PageNo.']
	page=int(re.findall('\d+',page)[0])
	table2=pd.DataFrame(table)
	table2=table2.sort_values([str(sorte)],ascending=('Ascending'==order))
	table2=table2.astype('str')
	if(100*(page)<len(table2.index)):
		x=100*(page-1)
		y=100*page
	elif(100*(page-1)>len(table2.index)):
		return render_template('goback.html')
	else:
		x=100*(page-1)
		y=len(table2.index)
	return render_template('sortpg.html',table=table2,table1=table2[x:y].to_html(),page=page)



y=100
@app.route('/data_search_result',methods=['POST'])
def search():
	global col
	global text
	col=request.form['search_col']
	text=request.form['text']
	col=str(col)
	text=str(text)
	global table
	table2=pd.DataFrame(table)
	table2=table2.astype('str')
	table2 = table2[table2[col].str.contains(text)]
	return render_template('search.html',table=table2,table1=table2[:100].to_html(),page=int(y/100))


@app.route('/data_search_page',methods=['POST'])
def search_page():
	global table
	page=request.form['PageNo.']
	page=int(re.findall('\d+',page)[0])
	table2=pd.DataFrame(table)
	table2=table2.astype('str')
	global col
	global text
	col=str(col)
	text=str(text)
	table2 = table2[table2[col].str.contains(text)]

	if(100*(page)<len(table2.index)):
		x=100*(page-1)
		y=100*page
	elif(100*(page-1)>len(table2.index)):
		return render_template('goback1.html')
	else:
		x=100*(page-1)
		y=len(table2.index)


	return render_template('searchpg.html',table=table2,table1=table2[x:y].to_html(),page=page)

z=100
@app.route('/sorted_search_result',methods=['POST'])
def search_sorted_data():
	global sorte
	global order
	sorte=request.form['column']
	order=request.form['order']
	sorte=str(sorte)
	order=str(order)
	global table
	table2=pd.DataFrame(table)
	table2=table2.sort_values([str(sorte)],ascending=('Ascending'==order))
	table2=table2.astype('str')
	table2 = table2[table2[col].str.contains(text)] 
	return render_template('sorted_search.html',table=table2,table1=table2[:100].to_html(),page=int(z/100))

@app.route('/sorted_search_page',methods=['POST'])
def search_sort_page():
	page=request.form['PageNo.']
	page=int(re.findall('\d+',page)[0])
	global tablename
	global sorte
	global order
	table2=pd.DataFrame(table)
	table2=table2.sort_values([str(sorte)],ascending=('Ascending'==order))
	table2=table2.astype('str')
	table2 = table2[table2[col].str.contains(text)] 
	if(100*(page)<len(table2.index)):
		x=100*(page-1)
		y=100*page
	elif(100*(page-1)>len(table2.index)):
		return render_template('goback2.html')
	else:
		x=100*(page-1)
		y=len(table2.index)

	return render_template('searchsortpg.html',table=table2,table1=table2[x:y].to_html(),page=page)	


@app.route('/about')
def about():
	return "<h1>We need no introduction.#AdiKumRach</h1>"

@app.route('/predict',methods=['POST'])
def predict():
	import pyodbc

	master_list1=[]
	batch_id=0
	today=date.today()
	start_time=time.time()




	batchName=request.form["batchName"]
	processStage=request.form["processStage"]
	folderName=request.form["folderName"]
	noOfArticles=request.form["noOfArticles"]

	master_list1.append(batchName)
	master_list1.append(processStage)
	master_list1.append(noOfArticles)	

	from database3 import insert_db_master1
	insert_db_master1(master_list1,batch_id)

	source=os.listdir(folderName)
	if(int(noOfArticles)>len(source)):
		noOfArticles=str(len(source))


	if processStage=="SFIVE":
		for file in source[:int(noOfArticles)]:
			print(file)
			#print("file-",file)
			sys.path.insert(0, r'C:\Users\digiscape\Desktop\batch\Batch_App_SmartQC\main_codes')
			from main import Batch_S5
			sys.path.insert(0, r'C:\Users\digiscape\Desktop\batch\Batch_App_SmartQC')
			from database3 import find_batch_id
			batch_id=find_batch_id()
			Batch_S5(folderName+"/"+file,batch_id)




	# master_list1.append(batchName)
	# master_list1.append(processStage)
	# master_list1.append(today)
	# master_list1.append(noOfArticles)

	# #master_list1.append(folderName)
	# master_list1.append(start_time)
	# master_list1.append(time.time())
	#print(time.time()-start_time)
	# print(str(today))
	#master_list1.append(str(today))
	master_list1=[]
	master_list1.append((time.time()-start_time))

	
	#from database3 import insert_db_master1
	#print(batch_id,"$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
	insert_db_master1(master_list1,batch_id)
	# cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=INSERT IP NUMBER;DATABASE=INSERT DATABASE NAME;UID=INSERT USER NAME;PWD=INSERT PASSWORD')

	# if(processStage=="CE"):



	# import os
	# source=os.listdir(folderName)
	# for filename in source:
	# 	master_list.append(filename)



	return "Data Stored"
	



if __name__ == '__main__':
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname) 
        app.run(host=IPAddr,port=7500,debug=True,use_reloader=True)
        app.config["TEMPLATES_AUTO_RELOAD"] = True
       #app.run(debug=True)
