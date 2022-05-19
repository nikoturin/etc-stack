#!/bin/Bash

echo "Configure QUEUES"
docker exec etc-stack_mq_1 rabbitmqctl add_vhost dev
docker exec etc-stack_mq_1 rabbitmqctl set_permissions -p dev guest ".*" ".*" ".*"
docker exec etc-stack_mq_1 rabbitmqadmin declare exchange --vhost=dev name=GTW-INTEROP type=direct
docker exec etc-stack_mq_1 rabbitmqadmin declare exchange --vhost=dev name=OPERADORAS type=direct
docker exec etc-stack_mq_1 rabbitmqadmin declare queue --vhost=dev name=DHL durable=true
docker exec etc-stack_mq_1 rabbitmqadmin declare queue --vhost=dev name=OPER1 durable=true
docker exec etc-stack_mq_1 rabbitmqadmin declare queue --vhost=dev name=OPER2 durable=true
docker exec etc-stack_mq_1 rabbitmqadmin declare queue --vhost=dev name=OPER3 durable=true
docker exec etc-stack_mq_1 rabbitmqadmin --vhost=dev declare binding source=GTW-INTEROP destination_type=queue destination=DHL routing_key=DELIVERY
docker exec etc-stack_mq_1 rabbitmqadmin --vhost=dev declare binding source=OPERADORAS destination_type=queue destination=OPER1 routing_key=OPER1
docker exec etc-stack_mq_1 rabbitmqadmin --vhost=dev declare binding source=OPERADORAS destination_type=queue destination=OPER2 routing_key=OPER2
docker exec etc-stack_mq_1 rabbitmqadmin --vhost=dev declare binding source=OPERADORAS destination_type=queue destination=OPER3 routing_key=OPER3

#sleep 5;
#echo "Process:Send.py"
#sendA=$(docker exec etc-stack_mq_1 cat /etc/hosts | tail -n 1);ip=$(echo $sendA|cut -d " " -f1);repIpSend=$(grep host /opt/etc-stack/mq/rabbitmq/src/send.py | cut -d "," -f1| cut -d "(" -f2); sed -i "s/$repIpSend/host='$ip'/" /opt/etc-stack/mq/rabbitmq/src/send.py

#sleep 5;
#echo "Process:Receive.py"
#recA=$(docker exec etc-stack_mq_1 cat /etc/hosts | tail -n 1);ip=$(echo $recA|cut -d " " -f1);repIpRec=$(grep pika.Connection /opt/etc-stack/mq/rabbitmq/src/receive.py | cut -d "," -f1| cut -d "(" -f3|tail -n 1);sed -i "s/$repIpRec/host='$ip'/" /opt/etc-stack/mq/rabbitmq/src/receive.py

#sleep 5;
#echo "Process:2Receive.py"
#recB=$(docker exec etc-stack_mq_1 cat /etc/hosts | tail -n 1);ip=$(echo $recB|cut -d " " -f1);repIpRec=$(grep pika.Connection /opt/etc-stack/mq/rabbitmq/src/oper2Receive.py | cut -d "," -f1| cut -d "(" -f3|tail -n 1);sed -i "s/$repIpRec/host='$ip'/" /opt/etc-stack/mq/rabbitmq/src/oper2Receive.py

#sleep 5;
#echo "Process:3Receive.py"
#recC=$(docker exec etc-stack_mq_1 cat /etc/hosts | tail -n 1);ip=$(echo $recC|cut -d " " -f1);repIpRec=$(grep pika.Connection /opt/etc-stack/mq/rabbitmq/src/oper3Receive.py | cut -d "," -f1| cut -d "(" -f3|tail -n 1);sed -i "s/$repIpRec/host='$ip'/" /opt/etc-stack/mq/rabbitmq/src/oper3Receive.py


#sleep 5;
#docker-compose stop pub && docker-compose stop sub

#sleep 5;
#docker-compose -f docker-compose.yaml up pub -d && 
docker-compose up -d sub
