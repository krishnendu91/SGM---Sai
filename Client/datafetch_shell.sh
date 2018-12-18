#!/bin/bash

#script to keep dimis alive

while [ true ]; do
{
date
./home/pi/SGM_Local/Client/Datafetch_dimis.py
sleep 10
} >> /home/pi/SGM_log/datafetch.log
done
