cat /etc/hosts
exit
ps faux
exit
rabbitmqctl add_vhost my_vhost
rabbitmqctl add_vhost dev
rabbitmqctl set_permissions -p dev guest ".*" ".*" ".*"
rabbitmqadmin declare exchange --vhost=dev name=ROUT-OPER5 type=direct
rabbitmqadmin declare queue --vhost=dev name=OPER5-TEST durable=True
rabbitmqadmin declare queue --vhost=dev name=OPER5-TEST durable=true
rabbitmqadmin --vhost=dev declare binding source=ROUT-OPER5 destination_type=queue destination=OPER5-TEST routing_key=TESTING
exit
sh /var/script/rabbitmq/queue.sh 
exit
