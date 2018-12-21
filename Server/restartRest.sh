#!/bin/bash
echo "Restart Process Initiated..."
echo "#############################################"
sleep 1
echo "Please be patient...."

service mosquitto stop
systemctl stop SMG_Server.service 
systemctl stop rest.service 
#service grafana-server stop 
#service mysql stop
#sleep 1

echo "Stop completed"

#service mysql start
service mosquitto start
systemctl start SMG_Server.service
systemctl start rest.service
#service grafana-server start

echo "Reboot success"
echo "Bye-Bye!"
