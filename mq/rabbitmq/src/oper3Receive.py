#!/usr/bin/env python
import pika, sys, os
import psycopg2


def main():

    con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="192.168.56.105",port="5432");
    cur = con.cursor();

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.105',port='5672',virtual_host='dev'))
    channel = connection.channel()
    
    channel.queue_declare(queue='OPER3',durable=True)

    def callback(ch, method, properties, body):

        print(" [x] Received %r" % body)
        data = body.decode()
        #print(data)
        carril = str(data[0:4])
        fecha  = str(data[4:12])
        hora_plaza = str(data[12:18])
        antena = str(data[18:28])
        tag = str(data[28:42])
        estatus = str(data[42:44])
        cruce = str(data[44:46])
        eje = str(data[46:48])
        rodada = str(data[48:51])
        clase = str(data[51:53])
        evento_carril = str(data[53:63])
        t_vehiculo = str(data[63:65])
        turno = str(data[65:66])
        sentido = str(data[66:67])
        fecha_hora_utc = str(data[67:81])

        sys_date=datetime.datetime.now()
        sqlValues = carril+","+fecha+","+hora_plaza+","+antena+",'"+tag+"',"+estatus+","+cruce+","+eje+","+rodada+","+clase+","+evento_carril+","+t_vehiculo+","+turno+",'"+sentido+"',"+fecha_hora_utc+",'"+sys_date+"'"

        #every message will be added to database independent 
        cur.execute("INSERT INTO oper3 (id, CARRIL,FECHA,HORA_PLAZA,ANTENA,TAG,ESTATUS,CRUCE,EJE,RODADA,CLASE,EVENTO_CARRIL,T_VEHICULO,TURNO,SENTIDO,FECHA_HORA_UTC,SYS_DATE) values (2,"+sqlValues+")");

        con.commit()

    channel.basic_consume(queue='OPER3', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
