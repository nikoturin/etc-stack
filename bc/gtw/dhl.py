import psycopg2

con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="192.168.56.105",port="5432");

print("Database opened successfully");

cur = con.cursor();

cur.execute("INSERT INTO cruces (id, CARRIL,FECHA,HORA_PLAZA,ANTENA,TAG,ESTATUS,CRUCE,EJE,RODADA,CLASE,EVENTO_CARRIL,T_VEHICULO,TURNO,SENTIDO,FECHA_HORA_UTC) values (2,'2308','20220202','130634','0000089494','OPER2-22939979','01','00','05','001','05','0000092546','02',2,'B','20160221200634')");

con.commit();
print("Record inserted successfully") 
con.close()
