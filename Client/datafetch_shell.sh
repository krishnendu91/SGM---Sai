#!/bin/bash

#script to keep dimis alive

while [true]; do
{
data
./Datafetch_dimis.py
sleep 5
} >> /home/pi/SGM_log/datafetch.log
done
