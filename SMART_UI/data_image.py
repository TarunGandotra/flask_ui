# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 09:42:03 2020

@author: Digiscape
"""

import pandas as pd
import numpy as np
import pypyodbc
import matplotlib.pyplot as plt
from configparser import ConfigParser

def load_configuration(file_path):
    config = ConfigParser(allow_no_value=True)
    config.read(file_path)
    return config

config = load_configuration(r"C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\main_codes\file\settings.ini")

database=str(config["DATABASE"]["database"])
connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
CU=[]
cursor = connection.cursor()
sql_query_CU="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_CU'"
sql_query_CU2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_CU' and ARTICLE_EXECUTION_COUNTER>1"
b=cursor.execute(sql_query_CU)
for i in b:
    CU.append(i[0])
#listReturn = []
#print(x,'jjkjkjkkjk')
#z = b.fetchone()
#listReturn.append(z[0])
#print(' c is ----',z[0])


p=cursor.execute(sql_query_CU2)
for j in p:
    CU.append(j[0])
print('list for CU',CU)
print('='*50)
#f = p.fetchone()
#listReturn.append(f[0])
#print(' d is ----',f[0])
AS=[]
sql_query_AS="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_S5'"
sql_query_AS2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_S5' and ARTICLE_EXECUTION_COUNTER>1"
As_1=cursor.execute(sql_query_AS)
for a in As_1:
    AS.append(a[0])
As_2=cursor.execute(sql_query_AS2)
for i in As_2:
    AS.append(i[0])
    
print('list for AS',AS)
print('='*50)

CE=[]
sql_query_CE="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_CE'"
sql_query_CE2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_CE' and ARTICLE_EXECUTION_COUNTER>1"
Ce_1=cursor.execute(sql_query_CE)
for a in Ce_1:
    CE.append(a[0])
Ce_2=cursor.execute(sql_query_CE2)
for i in Ce_2:
    CE.append(i[0])
    
print('list for CE',CE)
print('='*50)

Art=[]
sql_query_Art="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_ART'"
sql_query_Art2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast(getdate() as Date) and STAGE = 'UNIQ_ART' and ARTICLE_EXECUTION_COUNTER>1"
art_1=cursor.execute(sql_query_Art)
for a in art_1:
    Art.append(a[0])
art_2=cursor.execute(sql_query_Art2)
for i in art_2:
    Art.append(i[0])
    
print('list for Art',Art)
print('='*50)
# for i in b:
#     print(type(i))
#     #i[i.find("(")+1:i.find(")")]
#     c.append(i)
#     d.append(c[0][0])

#print('final list is ',listReturn.append(z[0]))
def data_image(CU,AS,CE,Art):
    print('image for CU')
    s_CU = pd.Series(CU)
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    ax.set_title('UNIQ_CU REPORT')
   
    s_CU.plot.bar()
    labels = ['TOTAL ', 'MODIFIED ']
    ax.set_xticklabels(labels)
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
    plt.yticks(np.arange(0, 300, step=50))
    plt.grid( which='major', linestyle='--')
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_CU.png')
    
    print('image for AS')
    s_AS = pd.Series(AS)
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    ax.set_title('UNIQ_S5 REPORT')
    #fig, ax = plt.subplots()
    s_AS.plot.bar()
    labels = ['TOTAL ', 'MODIFIED ']
    ax.set_xticklabels(labels)
    plt.setp(ax.get_xticklabels() , rotation=0, ha="center", rotation_mode="anchor")
    plt.yticks(np.arange(0, 300, step=50))
    plt.grid( which='major', linestyle='--')
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_AS.png')
    

    print('image for CE')
    s_CE = pd.Series(CE)
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    ax.set_title('UNIQ_CE REPORT')
    #fig, ax = plt.subplots()
    s_CE.plot.bar()
    labels = ['TOTAL ', 'MODIFIED ']
    ax.set_xticklabels(labels)
    plt.setp(ax.get_xticklabels() , rotation=0, ha="center", rotation_mode="anchor")
    plt.yticks(np.arange(0, 300, step=50))
    plt.grid( which='major', linestyle='--')
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_CE.png')
    

    print('image for Art')
    s_Art = pd.Series(Art)
    fig, ax = plt.subplots(figsize=(3.5,3.5))
    ax.set_title('UNIQ_ART REPORT')
    
    s_Art.plot.bar()
    labels = ['TOTAL ', 'MODIFIED ']
    ax.set_xticklabels(labels)
    
    
    plt.setp(ax.get_xticklabels(), rotation=0, ha="center", rotation_mode="anchor")
    plt.yticks(np.arange(0, 300, step=50))
    plt.grid( which='major', linestyle='--')
    colors = ['b','r']
		#for xtick, color in zip(ax.get_xticklabels(), colors):
	    #	xtick.set_color(color)
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_Art.png')


#a=[1,2,3]
data_image(CU,AS,CE,Art)