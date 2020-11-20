def insert_db_master1(out_list,batch_id):
	import pyodbc
	import datetime
	time = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
	connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=smart_qc;uid=sa;pwd=p@ssw0rd')
	cursor = connection.cursor()
	if batch_id==0:
		return_curs = cursor.execute('INSERT INTO batch_smartqc (BATCH_NAME,PROCESS_STAGE,CURR_DATE,NO_OF_ARTICLE) VALUES (?,?,?,?)',(out_list[0],out_list[1],time,out_list[2]))
	else:
		return_curs = cursor.execute('UPDATE batch_smartqc SET EXECUTION_TIME ='+str(out_list[0])+' '+'WHERE ID ='+str(batch_id)+';')


	#return_curs = cursor.execute('INSERT INTO batch_smartqc (BATCH_NAME,PROCESS_STAGE,CURR_DATE,NO_OF_ARTICLE,START_TIME,END_TIME,EXECUTION_TIME) VALUES (?,?,?,?,?,?,?)',(out_list[0],out_list[1],out_list[2],out_list[3],out_list[4],out_list[5],out_list[6]))
	connection.commit()
	return

def find_batch_id():
	import pyodbc
	connection = pyodbc.connect('Driver={SQL Server};Server=172.16.0.61;Database=smart_qc;uid=sa;pwd=p@ssw0rd')
	cursor = connection.cursor()
	stmt_counter = "SELECT MAX(ID) FROM BATCH_SMARTQC"
	return_curs = cursor.execute(stmt_counter)

	k = return_curs.fetchone()
	return k[0] 