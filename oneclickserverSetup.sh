#!/usr/bin/env bash

#one click new server setup

apt update
apt upgrade

apt install python3
apt install python3-pip

apt install apache2
apt install mysql-server
apt install phpmyadmin

pip3 install flask
pip3 install pymysql
pip3 install flask-mysql


