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


# for i in b:
#     print(type(i))
#     #i[i.find("(")+1:i.find(")")]
#     c.append(i)
#     d.append(c[0][0])

#print('final list is ',listReturn.append(z[0]))

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%f' % float(height),ha='center', va='bottom')


def date_data_image(param_date):
    #new_date=(str(param_date))
    config = load_configuration(r"C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\main_codes\file\settings.ini")

    database=str(config["DATABASE"]["database"])
    connection = pypyodbc.connect('Driver={'+config["DATABASE"]["server"]+'};Server='+config["DATABASE"]["hostname"]+';Database='+config["DATABASE"]["database"]+';uid='+config["DATABASE"]["username"]+';pwd='+config["DATABASE"]["password"])
    CU=[]

    cursor = connection.cursor()

    sql_query_CU="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_CU'"
    sql_query_CU2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_CU' and ARTICLE_EXECUTION_COUNTER>1"
    print('sql_query_CU--------------------------------'+sql_query_CU)
    print('sql_query_CU2-----------------------'+sql_query_CU2)
    b=cursor.execute(sql_query_CU)
    for i in b:
        CU.append(i[0])
    p=cursor.execute(sql_query_CU2)
    for j in p:
        CU.append(j[0])
    print('list for CU',CU)
    print('='*50)

    AS=[]
    sql_query_AS="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_S5'"
    sql_query_AS2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_S5' and ARTICLE_EXECUTION_COUNTER>1"
    As_1=cursor.execute(sql_query_AS)
    for a in As_1:
        AS.append(a[0])
    As_2=cursor.execute(sql_query_AS2)
    for i in As_2:
        AS.append(i[0])
        
    print('list for AS',AS)
    print('='*50)

    CE=[]
    sql_query_CE="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_CE'"
    sql_query_CE2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_CE' and ARTICLE_EXECUTION_COUNTER>1"
    Ce_1=cursor.execute(sql_query_CE)
    for a in Ce_1:
        CE.append(a[0])
    Ce_2=cursor.execute(sql_query_CE2)
    for i in Ce_2:
        CE.append(i[0])
        
    print('list for CE',CE)
    print('='*50)

    Art=[]
    sql_query_Art="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_ART'"
    sql_query_Art2="select count(*) from uniqmaster where cast(ITEMPROCESSING_MODIFIED_DATE as Date) = cast('"+param_date+"' as Date) and STAGE = 'UNIQ_ART' and ARTICLE_EXECUTION_COUNTER>1"
    art_1=cursor.execute(sql_query_Art)
    for a in art_1:
        Art.append(a[0])
    art_2=cursor.execute(sql_query_Art2)
    for i in art_2:
        Art.append(i[0])
        
    print('list for Art',Art)
    print('='*50)




    print('image for CU')
   # print('Chart Date is '+str(param_date))
    s_CU = pd.Series(CU)
    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np


    labels = ['Total','Modified']
    men_means = list(s_CU)

    x = np.arange(len(labels))  # the label locations
    width = 0.1  # the width of the bars

    fig, ax = plt.subplots(figsize=(2.7,2.7))
    rects1 = ax.bar(x - width/2, men_means, width=.7)


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('No of Articles')
    ax.set_title('UNIQ_CU-REPORT')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
#fig.tight_layout()
    plt.ylim(0, 300,50)
   # plt.show()
    #plt.grid( which='major', linestyle='--')
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_CU.png')
    
    print('image for AS')
    s_AS = pd.Series(AS)
    labels = ['Total','Modified']
    men_means = list(s_AS)

    x = np.arange(len(labels))  # the label locations
    width = 0.1  # the width of the bars

    fig, ax = plt.subplots(figsize=(2.7,2.7))
    rects1 = ax.bar(x - width/2, men_means, width=.7)


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('No of Articles')
    ax.set_title('UNIQ_S5-REPORT')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
#fig.tight_layout()
    plt.ylim(0, 300,50)
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_AS.png')
    

    print('image for CE')
    s_CE = pd.Series(CE)
    labels = ['Total','Modified']
    men_means = list(s_CE)

    x = np.arange(len(labels))  # the label locations
    width = 0.1  # the width of the bars

    fig, ax = plt.subplots(figsize=(2.7,2.7))
    rects1 = ax.bar(x - width/2, men_means, width=.7)


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('No of Articles')
    ax.set_title('UNIQ_CE-REPORT')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
#fig.tight_layout()
    plt.ylim(0, 300,50)
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_CE.png')
    

    print('image for Art')
    s_Art = pd.Series(Art)
    labels = ['Total','Modified']
    men_means = list(s_Art)

    x = np.arange(len(labels))  # the label locations
    width = 0.1  # the width of the bars

    fig, ax = plt.subplots(figsize=(2.7,2.7))
    rects1 = ax.bar(x - width/2, men_means, width=.7)


    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('No of Articles')
    ax.set_title('UNIQ_ART-REPORT')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()


    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 2),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')
    autolabel(rects1)
#fig.tight_layout()
    plt.ylim(0, 300,50)
    dest=r'C:\Users\Administrator\Desktop\update_ui\Batch_App_SmartQC\static'
    fig.savefig(dest+'\my_plot_Art.png')


