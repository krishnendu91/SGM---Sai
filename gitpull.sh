echo "Update process begins..."
echo "#############################################"
sleep 0.3
echo "Please be patient...."

{
cd /home/cs/SGM/
git pull
sleep 0.3
} >> /home/cs/updatelogs/github_pull.log
echo "Github update completed"
echo "updating local repository"
{
chmod 777 /home/cs/SGM/Client/*
chmod 777 /home/cs/SGM/AGG/*
cp /home/cs/SGM/Client/* /home/cs/SGM_Local/Client/
cp /home/cs/SGM/AGG/* /home/cs/SGM_Local/AGG/
cp /home/cs/SGM/Client/STP/* /home/cs/SGM_Local/Client/STP/
sleep 0.2
} >> /home/cs/updatelogs/local_copy.log

echo "copy to local repository completed"
{
cd /home/cs/SGM_Local/
git add .
git commit -m "auto updated"
sleep 0.3
echo "Local commit success"
} >> /home/cs/updatelogs/local_update.log

echo "Updation Process Complete." 
sleep 0.3
echo "Use git pull on client"
echo "Bye-Bye!"
