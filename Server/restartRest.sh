#!/bin/bash
echo "Restart Process Initiated..."
echo "#############################################"
sleep 0.5
echo "Please be patient...."

{
systemctl stop SMG_Server.service
systemctl stop mosquitto.service
#service mosquitto restart
#service SMG_Server restart
#service rest restart
}>> /home/cs/SGM_log/restartRest.log

#service grafana-server stop 
#service mysql stop
#sleep 1

#echo "Stop completed"

#service mysql start
#service mosquitto start
systemctl start mosquitto.service
systemctl start SMG_Server.service
#systemctl start rest.service
#service grafana-server start

echo "Reboot success"
echo "Bye-Bye!"
