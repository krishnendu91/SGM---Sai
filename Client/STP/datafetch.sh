#!/bin/bash


while [ true ]; do
{
date
/home/pi/SGM_Local/Client/STP/Datafetch_sch.py
sleep 5
} >> /home/pi/SGM_log/datafetch.log
done
