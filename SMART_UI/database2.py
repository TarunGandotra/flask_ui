def insert_db_master1(out_list):
    import pyodbc
    connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=testdata;uid=sa;pwd=p@ssw0rd')
    cursor = connection.cursor()
    
    return_curs = cursor.execute('INSERT INTO input1 (Name,Process,Articles,Parent_Folder,CurrentDate,Time_to_execute_in_sec) VALUES (?,?,?,?,?,?)',(out_list[0],out_list[1],out_list[2],out_list[3],out_list[4],out_list[5]))
        
    connection.commit()
    return