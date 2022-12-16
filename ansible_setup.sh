#!/bin/bash

yum -y install python3-pip
pip3 install pip --upgrade
pip3 install ansible --upgrade
pip3 install -r requirements.txt
ansible-galaxy install -r requirements.yml
