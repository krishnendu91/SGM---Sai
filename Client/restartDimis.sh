{
service mosquitto restart
service SGM_Client_api restart
service datafetch restart
echo "Service Restart Complete"
}>> /home/pi/SGM_log/restartDimis.log
