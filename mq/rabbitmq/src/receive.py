#!/usr/bin/env python
import pika, sys, os
import psycopg2
import asyncio 
import os 
import near_api
import json
import datetime
import random

from hfc.fabric import Client
from config import NODE_URL

def sendToNEAR(msg):
    provider = near_api.providers.JsonProvider(NODE_URL)
    signer = near_api.signer.Signer(
                "test.near",
                near_api.signer.KeyPair(
                    "ed25519:23Gshxq5ZXNzV2X7K2QRfbet1z7wWnQh1n1btd6H9i3Qg8EnzYrSnVDFmx4WazQnZKVgTEEkJURZVYRKgx4Rpq8X"
            ))

    master_account = near_api.account.Account(
                provider,
                signer,
                "test.near"
            )

    read = provider.view_call("test.near","get_status", json.dumps({"account_id": "test.near"}).encode('utf8'))
    read["result"] = json.loads(''.join([chr(x) for x in read["result"]]))
    print(read)

    trans = master_account.function_call("test.near","set_status",{"message": msg})
    print(trans)

def sendToHyper(operaName,msg):

    #get_event_loop() deprecated to python3.10 
    loop = asyncio.get_event_loop() 
    #loop = asyncio.new_event_loop()

    cli = Client(net_profile='network.json') 
    org1_admin = cli.get_user('org1.example.com', 'Admin')

    cli.new_channel('mychannel')


    gopath_bak = os.environ.get('GOPATH', '') 
    gopath = os.path.normpath(os.path.join(                       
            os.path.dirname(os.path.realpath('__file__'))                      
            )) 
    os.environ['GOPATH'] = os.path.abspath(gopath)

    rand = str(random.random())
    assetNo = int(rand[2:5])
    args = ["asset"+str(assetNo),"brown","100",operaName,"2000",msg]

    response = loop.run_until_complete(cli.chaincode_invoke(         
                requestor=org1_admin,         
                channel_name='mychannel',         
                peers=['peer0.org1.example.com','peer0.org2.example.com'],         
                args=args,         
                cc_name='basic',         
                fcn='CreateAsset',         
                transient_map=None,
                wait_for_event=True        
                 ))
    print("Error:" + response)

def sendToOpera(operaName,msg):

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.105',port='5672',virtual_host='dev'))
    channel = connection.channel()

    channel.queue_declare(queue=operaName, durable=True)
    channel.basic_publish(exchange="OPERADORAS", routing_key=operaName, body=msg)

    connection.close()

def main():
    
    con = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="192.168.56.105",port="5432");
    cur = con.cursor();

    connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.56.105',port='5672',virtual_host='dev'))
    channel = connection.channel()
    
    channel.queue_declare(queue='DHL',durable=True)
    
    def callback(ch, method, properties, body):

        print(" [x] Received %r" % body)
        data = body.decode()
        print(data)
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

        sqlValues = carril+","+fecha+","+hora_plaza+","+antena+",'"+tag+"',"+estatus+","+cruce+","+eje+","+rodada+","+clase+","+evento_carril+","+t_vehiculo+","+turno+",'"+sentido+"',"+fecha_hora_utc+",'"+str(sys_date)+"'"

       
        operType=tag.split("-")

        #Sending message ETC to Private BC HyperLedger
        print("Oper:"+operType[0]+" Data:"+data)
        sendToHyper(operType[0],data)

        #Sending message ETC to Public BC NEAR
        sendToNEAR(data)

        #Sendig message ETC to Operator 
        sendToOpera(operType[0],data)

        #every message will be added to database independent 
        cur.execute("INSERT INTO cruces (id, CARRIL,FECHA,HORA_PLAZA,ANTENA,TAG,ESTATUS,CRUCE,EJE,RODADA,CLASE,EVENTO_CARRIL,T_VEHICULO,TURNO,SENTIDO,FECHA_HORA_UTC,SYS_DATE) values (2,"+sqlValues+")");

        con.commit()

    channel.basic_consume(queue='DHL', on_message_callback=callback, auto_ack=True)

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
