#!/usr/bin/env python
import pika
import random

#etc = "2308202202021306340000089494OPER3-22939979010005001050000092546022B20160221200634"
etc = ''
opers = [1,2,3]

rand = str(random.random())
oper = int(rand[2:3])
    
if oper in opers:
    stts = oper
    etc = "2308202202021306340000089494OPER" + str(oper) + "-22939979010005001050000092546022B20160221200634"
    
    connection = pika.BlockingConnection(
            pika.ConnectionParameters(host='192.168.56.105',port='5672',virtual_host='dev'))
    channel = connection.channel()

    channel.queue_declare(queue='DHL',durable=True)

    channel.basic_publish(exchange='GTW-INTEROP', routing_key='DELIVERY', body=etc)
    #body='Random number: ' + str(rand))
    print(" [x] ELECTRONIC TOLL COLLECTOR DATA RAW STARTED ---->")
    connection.close()
else:
    print("TAG Number:%1d Not Passing my cards yet :("%oper)
