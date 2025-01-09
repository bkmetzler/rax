#!/bin/bash
#Make sure apt-get is fully non-interactive
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get install -y curl python-pip python-dev screen
echo "set nocompatible" > /root/.vimrc
pip install turbolift eventlet
uuidgen > /root/cloudqueueid.txt
