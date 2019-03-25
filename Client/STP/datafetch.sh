#!/bin/bash


while [ true ]; do
{
date
/home/pi/SGM_Local/Client/STP/Datafetch_sch.py
sleep 10
} >> /home/pi/SGM_log/datafetch.log
done
