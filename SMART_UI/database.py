def insert_db_master(out_list):
    connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=unitouch;uid=sa;pwd=p@ssw0rd')
    cursor = connection.cursor()
    stmt_counter = "SELECT COUNTER FROM uniqmaster WHERE UNIQITEMID ="+"\'"+uniq_item_id+"\'"+";"
    return_curs = cursor.execute(stmt_counter)

    k = return_curs.fetchone() 
    if k == None:
        params = ['?' for item in out_list]
        stmt= 'INSERT INTO uniqmaster (UNIQITEMID, USERID, JID, AID, STAGE,ITEMPROCESSINGDATE,ERRORCOUNT, COUNTER) VALUES (%s);' % ','.join(params)
        cursor.execute(stmt, out_list)
    else:
        count = k[0]+1
        cursor.execute("UPDATE uniqmaster SET COUNTER ="+str(count)+" "+"WHERE UNIQITEMID ="+"\'"+uniq_item_id+"\'"+";")
        #cursor.execute("UPDATE uniqmaster_1 SET ITEMPROCESSINGDATE ="+Start_time+" "+"WHERE UNIQITEMID ="+"\'"+uniq_item_id+"\'"+";")
        
    
    connection.commit()
    return;