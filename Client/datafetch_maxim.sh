#!/bin/bash

#script to read data from Maxim every 10s

while [ true ]; do
{
date
./home/pi/SGM_Local/Client/Datafetch_maxim.py
sleep 10
} >> /home/pi/SGM_log/datafetch.log
done
